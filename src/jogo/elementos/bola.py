
from graphics import GraphWin
from jogo.elementos.barra import Barra


class Bola:

    posicao_x: int
    posicao_y: int
    velocidade_x: float
    velocidade_y: float
    raio: int
    cor: str

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
        # TODO determinar valores x e y limite da bola que indicam
        # TODO conflito/colisão com a barra em questão.
        # ? Pode ser uma boa ideia usar só um dos lados da bola para se
        # ? evitar bugs. Imagine a situação em que a barra bate na bola
        # ? após ela passar. Também é uma alternativa travar os comandos
        # ? das barras uma vez que a bola passe da face da barra.

        # TODO determinar valores x e y da barra que levariam a
        # TODO conflito/colisão

        # TODO ajustar posição e velocidades da bolinha caso haja
        # TODO colisão
        pass
