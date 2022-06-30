

from hashlib import algorithms_available
from graphics import GraphWin, tk
from src.jogo.jogo import Jogo
from src.menu.menu import Menu
from src.ranking.ranking import Ranking


def rodar():

    # Encontra a resolução da tela
    root = tk.Tk()
    tela_largura = root.winfo_screenwidth()
    tela_altura = root.winfo_screenheight()
    root.destroy()

    # Inicializa janela do jogo
    janela_largura = tela_largura/2
    janela_altura = tela_altura/2
    janela = GraphWin("Nosso Pong", janela_largura, janela_altura)

    jogo = Jogo(janela)
    jogo.rodar(janela)

    # Loop do programa
    sair = False
    while not sair:
        menu = Menu()
        menu.rodar(janela)
        if menu.iniciar:
            jogo = Jogo()
            sair = jogo.rodar(janela)
        elif menu.ranking:
            ranking = Ranking()
            ranking.rodar(janela)
        elif menu.sair:
            sair = True


if __name__ == "__main__":
    rodar()
