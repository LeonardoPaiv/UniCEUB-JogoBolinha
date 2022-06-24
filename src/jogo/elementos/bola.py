
from graphics import GraphWin, Circle
from jogo.elementos.barra import Barra


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
            velocidade_x: int = 0,
            velocidade_y: int = 0,
            raio: int = 10,
            cor: str = 'black'
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
        self.raio += incremento
        # TODO Garantir que raio não é zero ou negativo

    def incrementar_posicao(self):
        """Incrementa a posicao com base nas velocidades
        "self.velocidade_x" e "self.velocidade_y"
        """
        self.posicao_x += self.velocidade_x
        self.posicao_y += self.velocidade_y

    def verificar_colisao(self, barra: Barra):
        """Verifica se alguma região da bola está em conflito com a
        barra nas coordenadas atuais.

        Args:
            barra (Barra): barra para verificar se houve colisão.
        """
        # TODO chamar método "self.verificar_interseccao" para avaliar
        # TODO se a posição atual da bolina intersecta com a posição da
        # TODO barra em questão.

        # TODO ajustar posição e velocidades da bolinha caso haja
        # TODO colisão
        pass

    def verificar_interseccao(self, barra: Barra) -> bool:
        """Verifica se há intersecção entre o desenho da bola e da
        barra em questão.

        Args:
            barra (Barra): barra para verificar se há intersecção

        Returns:
            bool: True caso haja intersecção.
        """
        # TODO determinar valores x e y limite da bola que levariam à
        # TODO indicação de intersecção com a barra em questão.

        # TODO determinar valores x e y da barra que levariam a
        # TODO indicação de intersecção.

        # TODO avaliar se há interesecção e retornar True, caso haja,
        # TODO ou False, caso não haja.
        pass
