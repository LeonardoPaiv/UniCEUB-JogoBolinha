
from graphics import GraphWin, Rectangle, Point


class Barra():

    posicao_x: int
    posicao_y: int
    velocidade_y: float
    largura: int
    altura: int
    altura_inical: int
    cor: str
    desenho: Rectangle

    def __init__(
            self,
            posicao_x: int = 0,
            posicao_y: int = 0,
            velocidade_y: int = 0,
            largura: int = 10,
            altura_inical: int = 100,
            cor: str = 'black'
            ) -> None:
        self.posicao_x = posicao_x
        self.posicao_y = posicao_y
        self.velocidade_y = velocidade_y
        self.largura = largura
        self.altura_inical = altura_inical
        self.altura = altura_inical
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

    def alterar_altura(self, janela, valor_alteracao: int) -> None:
        """Incrementa a altura da barra.

        Args:
            incremento (int): porcentagem de alteracao da altura da barra
            (pode ser negativo).
        """
        self.apagar_desenho()

        nova_tamanho_porcentagem = self.altura_inical * valor_alteracao / 100
        
        if  self.altura > 0.5 * self.altura_inical and self.altura < 1.5 * self.altura_inical:
            self.altura += nova_tamanho_porcentagem

        self.desenhar(janela)

    def descer(self, janela):
        """Incrementa a posição no eixo y com base em "self.velocidade"
        """
        self.apagar_desenho()
        self.posicao_y += self.velocidade_y
        self.desenhar(janela)

    def subir(self, janela):
        self.apagar_desenho()
        self.posicao_y -= self.velocidade_y
        self.desenhar(janela)

    def posicao_inicial_esq(self, janela: GraphWin):
        self.posicao_y = int((janela.getHeight() / 2) - (self.altura / 2))
        self.posicao_x = 30

    def posicao_inicial_dir(self, janela: GraphWin):
        self.posicao_y = int((janela.getHeight() / 2) - (self.altura / 2))
        self.posicao_x = janela.getWidth() - 30
