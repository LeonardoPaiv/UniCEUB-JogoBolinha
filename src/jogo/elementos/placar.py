from turtle import position
from graphics import GraphWin, Point, Text


class Placar:

    posicao_x: int
    posicao_y: int
    pontuacao_esquerda: int
    pontuacao_direita: int
    placar_jogo: Text

    def __init__(self, janela: GraphWin) -> None:
        self.posicao_x = int(janela.getWidth() / 2)
        self.posicao_y = int(janela.getHeight() / 2)
        self.pontuacao_esquerda = 0
        self.pontuacao_direita = 0

    def desenhar(self, janela: GraphWin):
        """Desenha o placar na janela do jogo.

        Args:
            janela (GraphWin): Janela na qual o programa está sendo
            executado.
        """
        # TODO desenhar placar na janela
        _tamanho_da_fonte = 36
        placar_jogo = Text(
            Point(self.posicao_x, self.posicao_y),
            str(self.pontuacao_esquerda) + ' : ' + str(self.pontuacao_direita)
            )
        placar_jogo.setSize(_tamanho_da_fonte)
        placar_jogo.draw(janela)
        pass

    def soma_ponto_player_esq(self):
        """Soma ponto para o jogador da esquerda
        """
        self.pontuacao_esquerda += 1
        self.apagar_placar_jogo()
        self.desenhar()

    def soma_ponto_player_dir(self):
        """Soma ponto para o jogador da direita
        """
        self.pontuacao_direita += 1
        self.apagar_placar_jogo()
        self.desenhar()

    def apagar_placar_jogo(self):
        """Apaga o desenho do placar.
        """
        self.placar_jogo.undraw()
