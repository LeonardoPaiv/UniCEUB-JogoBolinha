
from graphics import GraphWin, Rectangle, Point

class Campo():

    def __init__(self, janela: GraphWin) -> None:
        
        self.largura_janela = janela.getWidth()
        self.altura_janela = janela.getHeight()
        self.canto_esquerda = Rectangle(Point(0,0), Point(10, self.altura_janela))
        self.canto_direita = Rectangle(Point(self.largura_janela, 0), Point(self.largura_janela - 10, self.altura_janela))
        self.canto_superior = Rectangle(Point(0, 0), Point(self.largura_janela, 10))
        self.canto_inferior = Rectangle(Point(0, self.altura_janela), Point(self.largura_janela, self.altura_janela - 10))

        pass

    def desenhar_campo(self, janela: GraphWin):

        self.canto_esquerda.setFill('red')
        self.canto_esquerda.draw(janela)
        
        self.canto_direita.setFill('blue')
        self.canto_direita.draw(janela)

        self.canto_superior.setFill('black')
        self.canto_superior.draw(janela)

        self.canto_inferior.setFill('black')
        self.canto_inferior.draw(janela)

    def apagar_campo(self):

        self.canto_esquerda.undraw()
        
        self.canto_direita.undraw()

        self.canto_superior.undraw()

        self.canto_inferior.undraw()