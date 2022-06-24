from graphics import GraphWin, Text


class Placar:

    posicao_x: int
    posicao_y: int
    pontuacao_esquerda: int
    pontuacao_direita: int
    desenho: Text

    def __init__(self, posicao_x: int = 0, posicao_y: int = 0) -> None:
        self.posicao_x = posicao_x
        self.posicao_y = posicao_y
        self.pontuacao_esquerda = 0
        self.pontuacao_direita = 0

    def desenhar(self, janela: GraphWin):
        """Desenha o placar na janela do jogo.

        Args:
            janela (GraphWin): Janela na qual o programa está sendo
            executado.
        """
        # TODO desenhar placar na janela
        pass

    def apagar_desenho(self):
        """Apaga o desenho do placar.
        """
        self.desenho.undraw()
