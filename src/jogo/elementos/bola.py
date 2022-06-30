
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
        if (self.raio + incremento) <= 0: return

        self.raio += incremento

    def incrementar_posicao(self):
        """Incrementa a posicao com base nas velocidades
        "self.velocidade_x" e "self.velocidade_y"
        """
        self.posicao_x += self.velocidade_x
        self.posicao_y += self.velocidade_y

    def verificar_colisao(self, barra_esq: Barra, barra_dir: Barra, janela: GraphWin):
        """Verifica se alguma região da bola está em conflito com a
        barra nas coordenadas atuais.

        Args:
            barra (Barra): barra para verificar se houve colisão.
        """
        # TODO chamar método "self.verificar_interseccao_barra" para avaliar
        # TODO se a posição atual da bolina intersecta com a posição da
        # TODO barra em questão.
        colisao_barra_esq = self.verificar_interseccao_barra_esq(barra_esq)

        colisao_barra_dir = self.verificar_interseccao_barra_dir(barra_dir)

        colisao_campo = self.verificar_interseccao_campo(janela)

        ponto_jogador_esq = self.verificar_ponto_esq(janela)

        ponto_jogador_dir = self.verificar_ponto_dir()


        # TODO ajustar posição e velocidades da bolinha caso haja
        # TODO colisão
        if colisao_barra_esq or colisao_barra_dir: self.velocidade_x = -(self.velocidade_x)

        if colisao_campo: self.velocidade_y = -(self.velocidade_y)

        if ponto_jogador_esq:
            self.reset_bolinha(janela)
            return 'ponto_esq'


        if ponto_jogador_dir:
            self.reset_bolinha(janela)
            return 'ponto_dir'
         

        pass


    def verificar_interseccao_barra_esq(self, barra_esq: Barra) -> bool:
        """Verifica se há intersecção entre o desenho da bola e da
        barra em questão.

        Args:
            barra (Barra): barra para verificar se há intersecção

        Returns:
            bool: True caso haja intersecção.
        """
        # TODO determinar valores x e y limite da bola que levariam à
        # TODO indicação de intersecção com a barra em questão.
        altura_inicial_barra = barra_esq.posicao_y
        altura_final_barra = barra_esq.posicao_y + barra_esq.altura

        comprimento_inicial_barra = barra_esq.posicao_x
        comprimento_final_barra = barra_esq.posicao_x + barra_esq.largura


        # esse serve para barra direita
        if (self.posicao_x + self.raio) > (comprimento_inicial_barra) and (self.posicao_x + self.raio) < (comprimento_final_barra):
            if (self.posicao_y + self.raio) > (altura_inicial_barra) and (self.posicao_y - self.raio) < (altura_final_barra):
                return True

        # essa serve para barra esquerda
        if (self.posicao_x - self.raio) > (comprimento_inicial_barra) and (self.posicao_x - self.raio) < (comprimento_final_barra):
            if (self.posicao_y + self.raio) > (altura_inicial_barra) and (self.posicao_y - self.raio) < (altura_final_barra):
                return True

        return False

    def verificar_interseccao_barra_dir(self, barra_dir: Barra):

        altura_inicial_barra = barra_dir.posicao_y
        altura_final_barra = barra_dir.posicao_y + barra_dir.altura

        comprimento_inicial_barra = barra_dir.posicao_x
        comprimento_final_barra = barra_dir.posicao_x + barra_dir.largura


        # esse serve para barra direita
        if (self.posicao_x + self.raio) > (comprimento_inicial_barra) and (self.posicao_x + self.raio) < (comprimento_final_barra):
            if (self.posicao_y + self.raio) > (altura_inicial_barra) and (self.posicao_y - self.raio) < (altura_final_barra):
                return True

        # essa serve para barra esquerda
        if (self.posicao_x - self.raio) > (comprimento_inicial_barra) and (self.posicao_x - self.raio) < (comprimento_final_barra):
            if (self.posicao_y + self.raio) > (altura_inicial_barra) and (self.posicao_y - self.raio) < (altura_final_barra):
                return True

        return False


    def verificar_interseccao_campo(self, janela: GraphWin) -> bool:

        if (self.posicao_y - self.raio) < 10 or (self.posicao_y + self.raio) > janela.getHeight() - 10:
            return True

        return False
        pass

    def verificar_ponto_esq(self, janela: GraphWin):
        

        if self.posicao_x > int(janela.getWidth() + 50):
            return True
        return False
        pass

    def verificar_ponto_dir(self) -> None:

        if self.posicao_x < -50:
            return True
        return False
        pass

        

    def reset_bolinha(self, janela: GraphWin) -> None:

        self.posicao_x = int(janela.getWidth() / 2)
        self.posicao_y = int(janela.getHeight() / 2)
        self.velocidade_x = 10
        self.velocidade_y = 10
        self.raio = 10

        pass
