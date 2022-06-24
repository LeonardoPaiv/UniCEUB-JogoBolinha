
from graphics import GraphWin, Rectangle, Point


class Barra():

    posicao_x: int
    posicao_y: int
    velocidade_y: float
    largura: int
    altura: int
    cor: str
    desenho: Rectangle

    def __init__(
            self,
            posicao_x: int = 0,
            posicao_y: int = 0,
            velocidade_y: int = 0,
            largura: int = 10,
            altura: int = 50,
            cor: str = 'black'
            ) -> None:
        self.posicao_x = posicao_x
        self.posicao_y = posicao_y
        self.velocidade_y = velocidade_y
        self.largura = largura
        self.altura = altura
        self.cor = cor

    def desenhar(self, janela: GraphWin) -> None:
        """Desenha a barra na janela com base nos parâmetros self.

        Args:
            janela (GraphWin): Janela na qual o programa está sendo
            executado.
        """
        # TODO desenhar barra na janela com base nos parâmetros self.
        self.desenho = Rectangle(Point(self.posicao_x, self.posicao_y), Point(self.posicao_x + self.largura, self.posicao_y + self.altura))
        self.desenho.setFill(self.cor)
        self.desenho.draw(janela)

    def apagar_desenho(self) -> None:
        """Apaga o desenho da barra.
        """
        self.desenho.undraw()

    def incrementar_velocidade(self, incremento: float) -> None:
        """Incrementa a velocidade da barra.

        Args:
            incremento (float): valor de incremento da velocidade
            (pode ser negativo).
        """
        self.velocidade_y += incremento

    def incrementar_altura(self, incremento: int) -> None:
        """Incrementa a altura da barra.

        Args:
            incremento (int): valor de incremento da altura da barra
            (pode ser negativo).
        """
        # TODO garantir que altura não é negativa ou zero
        if (self.altura + incremento) <= 0: return

        self.altura += incremento

    def incrementar_posicao_y(self):
        """Incrementa a posição no eixo y com base em "self.velocidade"
        """
        self.posicao_y += self.velocidade_y
