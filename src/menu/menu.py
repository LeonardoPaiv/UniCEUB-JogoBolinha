from graphics import GraphWin


class Menu:

    continuar: bool
    iniciar: bool
    ranking: bool
    sair: bool
    _i_selecao: int
    _itens: list[str]

    def __init__(self) -> None:
        self.continuar = False
        self.iniciar = False
        self.ranking = False
        self.sair = False
        self._i_selecao = 0
        self._itens = []

    def rodar(self, janela: GraphWin, em_jogo: bool = False):
        """Roda o menu do jogo.

        Args:
            janela (GraphWin): Janela na qual o programa está sendo
            executado.
            em_jogo (bool?): Indica se há um jogo acontecendo ou não.
        """
        # TODO preencher lista de itens do menu "self._itens".
        # ! Caso um jogo esteja acontecendo, incluir a opção
        # ! "continuar". Caso contrário, não incluir essa opção.

        # Loop de leitura do menu
        selecionado = False
        while not selecionado:
            # TODO desenhar menu chamando o método "self.__desenhar"

            # TODO ler tecla do jogador

            # TODO caso a tecla seja a seta para cima "Up" ou "w",
            # TODO decrementar "self._i_selecao".
            # ! Caso "self._i_selecao" seja menor que a quantidade de
            # ! opções, não decrementar ou reiniciar do final da lista.

            # TODO caso a tecla seja a seta para baixo "Down" ou "s",
            # TODO incrementar "self._i_selecao".
            # ! Caso "self._i_selecao" seja maior que a quantidade de
            # ! opções, não incrementar ou reiniciar do início da lista.

            # TODO caso a tecla seja enter "Return", chamar o método
            # TODO "self.__executar_acao" e atualizar a variável
            # TODO "selecionado" para True (pois um item foi
            # TODO selecionado)
            break

        pass

    def __desenhar(self, janela: GraphWin) -> None:
        """Desenha o menu na tela do jogo. Os itens do menu estão
        contidos no dicionário "self.itens".

        Args:
            janela (GraphWin): Janela na qual o programa está sendo
            executado.
        """
        # TODO Limpa a janela.

        # TODO Desenha os itens do menu de opções de acordo com a lista
        # TODO "self._itens".
        # ! A opção selecionada "self._i_selecao" deve ser destacada.
        pass

    def __executar_acao(self) -> None:
        """Executa a ação associada ao item selecionado (identificado
        pelo parâmetro "self._i_selecao").
        """
        # TODO Atualizar o valor do parâmetro "self.continuar" para
        # TODO True caso "self.itens" de "self._i_selecao" continuar

        # TODO Atualizar o valor do parâmetro "self.iniciar" caso para
        # TODO True caso "self.itens" de "self._i_selecao" seja iniciar

        # TODO Atualizar o valor do parâmetro "self.ranking" caso para
        # TODO True caso "self.itens" de "self._i_selecao" seja ranking

        # TODO Atualizar o valor do parâmetro "self.sair" caso para
        # TODO True caso "self.itens" de "self._i_selecao" seja sair

        pass
