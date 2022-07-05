
from io import RawIOBase
from tokenize import Double
from graphics import GraphWin, Circle, Point
from src.jogo.elementos.barra import Barra
from src.jogo.elementos.placar import Placar


class Bola:

    posicao_x: int
    posicao_y: int
    velocidade_x: float
    velocidade_y: float
    raio: int
    cor: str
    desenho: Circle

    def __init__(
            self,
            posicao_x: int = 0,
            posicao_y: int = 0,
            velocidade_x: int = 10,
            velocidade_y: int = 10,
            raio: int = 10,
            cor: str = 'green'
            ) -> None:
        self.posicao_x = posicao_x
        self.posicao_y = posicao_y
        self.velocidade_x = velocidade_x
        self.velocidade_y = velocidade_y
        self.raio = raio
        self.cor = cor

    def desenhar(self, janela: GraphWin) -> None:
        """Desenha a barra na janela com base nos parâmetros self.

        Args:
            janela (GraphWin): Janela na qual o programa está sendo
            executado.
        """
        # TODO desenhar barra na janela com base nos parâmetros self.
        self.desenho = Circle(Point(self.posicao_x, self.posicao_y), self.raio)
        self.desenho.setFill(self.cor)
        self.desenho.draw(janela)

    def apagar_desenho(self) -> None:
        """Apaga o desenho da bola.
        """
        self.desenho.undraw()

    def incrementar_velocidade_x(self, incremento: float) -> None:
        """Incrementa a velocidade horizontal da barra.

        Args:
            incremento (float): valor de incremento da velocidade
            (pode ser negativo).
        """
        self.velocidade_x += incremento

    def incrementar_velocidade_y(self, incremento: float) -> None:
        """Incrementa a velocidade vertical da barra.

        Args:
            incremento (float): valor de incremento da velocidade
            (pode ser negativo).
        """
        self.velocidade_y += incremento

    def incrementar_raio(self, incremento: int) -> None:
        """Incrementa a altura da barra.

        Args:
            incremento (int): valor de incremento de raio da bola
            (pode ser negativo).
        """
        # TODO Garantir que raio não é zero ou negativo
        if (self.raio + incremento) <= 0:
            return

        self.raio += incremento

    def incrementar_posicao(self):
        """Incrementa a posicao com base nas velocidades
        "self.velocidade_x" e "self.velocidade_y"
        """
        self.posicao_x += self.velocidade_x
        self.posicao_y += self.velocidade_y

    def verificar_interseccao_barra(self, barra: Barra):
        inicio_vertical_barra = barra.posicao_y
        final_vertical_barra = barra.posicao_y + barra.altura

        inicio_horizontal_barra = barra.posicao_x
        fim_horizontal_barra = barra.posicao_x + barra.largura

        inicio_horizontal_bola = self.posicao_x - self.raio
        final_horizontal_bola = self.posicao_x + self.raio

        inicio_vertical_bola = self.posicao_y - self.raio
        final_vertical_bola = self.posicao_y + self.raio

        def colidiu_barra(coordenada_bola, orientacao):
            if (orientacao == "horizontal"):
                return coordenada_bola <= fim_horizontal_barra and coordenada_bola >= inicio_horizontal_barra
            else:
                return coordenada_bola <= final_vertical_barra and coordenada_bola >= inicio_vertical_barra

        def vai_colidir_barra():
            vai_colidir_indo_direita = (final_horizontal_bola < inicio_horizontal_barra 
                                        and final_horizontal_bola + self.velocidade_x >= inicio_horizontal_barra)
            vai_colidir_indo_esquerda = (inicio_horizontal_bola > fim_horizontal_barra 
                                        and inicio_horizontal_bola + self.velocidade_x <= fim_horizontal_barra)
            # print (f'vai colidir direita{vai_colidir_indo_direita}')
            # print (f'vai colidir esquerda{vai_colidir_indo_esquerda}')
            return vai_colidir_indo_direita or vai_colidir_indo_esquerda
            
        is_encostando_horizontal = (final_horizontal_bola == inicio_horizontal_barra
                                    or inicio_horizontal_bola == fim_horizontal_barra
                                    or vai_colidir_barra())
        is_encostando_vertical = (colidiu_barra(inicio_vertical_bola, "vertical") 
                                    or colidiu_barra(final_vertical_bola, "vertical"))

        is_encostando = is_encostando_horizontal and is_encostando_vertical

        return is_encostando

    def verificar_colisao(
            self,
            barra_esq: Barra,
            barra_dir: Barra,
            janela: GraphWin
            ) -> str:
        """Verifica se alguma região da bola está em conflito com a
        barra nas coordenadas atuais.

        Args:
            barra (Barra): barra para verificar se houve colisão.
        """
        # TODO chamar método "self.verificar_interseccao_barra" para avaliar
        # TODO se a posição atual da bolina intersecta com a posição da
        # TODO barra em questão.

        # TODO ajustar posição e velocidades da bolinha caso haja
        # TODO colisão

        colisao_barra_esq = self.verificar_interseccao_barra(barra_esq)
        colisao_barra_dir = self.verificar_interseccao_barra(barra_dir)

        if colisao_barra_esq or colisao_barra_dir:
            sinal_velocidade = self.velocidade_x / abs(self.velocidade_x)
            nova_velocidade = self.velocidade_x + 3 * sinal_velocidade # 3 é a taxa de aceleração
            self.velocidade_x = -(nova_velocidade)

        colisao_campo = self.verificar_interseccao_campo(janela)

        if colisao_campo: self.velocidade_y = -(self.velocidade_y)

        ponto_jogador_esq = self.verificar_ponto_esq(janela)
        ponto_jogador_dir = self.verificar_ponto_dir()

        if ponto_jogador_esq:
            self.reset_bolinha(janela)
            return 'ponto_esq'

        if ponto_jogador_dir:
            self.reset_bolinha(janela)
            return 'ponto_dir'

    def verificar_interseccao_campo(self, janela: GraphWin) -> bool:
        inicio_horizontal_bola = self.posicao_y - self.raio
        fim_horizontal_bola = self.posicao_y + self.raio

        is_bola_dentro_tela = inicio_horizontal_bola < 10 or fim_horizontal_bola > janela.getHeight() - 10

        return is_bola_dentro_tela

    def verificar_ponto_esq(self, janela: GraphWin):
        passou_barra_direita = self.posicao_x > int(janela.getWidth() + 50)
        return passou_barra_direita

    def verificar_ponto_dir(self) -> None:
        passou_barra_esquerda = self.posicao_x < -50
        return passou_barra_esquerda

    def reset_bolinha(self, janela: GraphWin) -> None:
        self.posicao_x = int(janela.getWidth() / 2)
        self.posicao_y = int(janela.getHeight() / 2)
        self.velocidade_x = 10
        self.velocidade_y = 10
        self.raio = 10
