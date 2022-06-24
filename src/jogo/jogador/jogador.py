
from graphics import GraphWin


class Jogador:

    nome: str
    pontuacao: int

    def __init__(self) -> None:
        self.nome = ""
        self.pontuacao = 0

    def rodar(self, janela: GraphWin) -> None:
        """Roda a parte do jogo que define o jogador.

        Args:
            janela (GraphWin): Janela na qual o programa está sendo
            executado.
        """
        # TODO Chamar o método "self.__desenhar" para desenhar a tela
        # TODO onde o jogador entra com seu nome.

        # Loop de leitura do nome do jogador
        nome_ok = False
        while not nome_ok:
            # TODO ler tecla do jogador

            # TODO caso a tecla seja enter "Return", atualizar a
            # TODO variável "nome_ok" para True (pois o jogador
            # TODO terminou de escrever seu nome).
            # ! Verificar se o nome não está vazio! Caso esteja,
            # ! desenhar uma mensagem para o jogador dizendo que o nome
            # ! não pode ser vazio ou algo assim.
            break

        # TODO Extrair texto do objeto Entry e armazenar em "self.nome"
        pass

    def __desenhar(self, janela: GraphWin):
        """Desenha a tela para entrada do nome do jogador.

        Args:
            janela (GraphWin): Janela na qual o programa está sendo
            executado.
        """
        # TODO Limpa a janela.

        # TODO Desenha campo onde o jogador digita seu nome usando Entry

        # TODO Desenha botão "OK" ou "Continuar" ou "Pronto" caso
        # TODO desejado. A ideia é que o jogador pressione "Enter" para
        # TODO prosseguir.
        pass

    def incrementar_pontuacao(self):
        """Incrementa a pontuação do jogador.
        """
        self.pontuacao += 1
