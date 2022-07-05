from graphics import GraphWin, Point, Text


class Menu:

    continuar: bool
    iniciar: bool
    ranking: bool
    sair: bool
    _i_selecao: int
    _itens: list[str]
    texts: list[Text]

    def __init__(self) -> None:
        self.continuar = False
        self.iniciar = False
        self.ranking = False
        self.sair = False
        self._i_selecao = 0
        self._itens = []
        self.texts = []

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
        if em_jogo:
            self._itens = ['Continuar']
        else:
            self._itens = ['Iniciar']
        self._itens.extend(['Ranking', 'Sair'])
        # Loop de leitura do menu
        selecionado = False
        mudanca_de_opcao = False
        self.__desenhar(janela)
        while not selecionado:
            # TODO desenhar menu chamando o método "self.__desenhar"
            # TODO ler tecla do jogador
            tecla = janela.checkKey()

            # TODO caso a tecla seja enter "Return", chamar o método
            # TODO "self.__executar_acao" e atualizar a variável
            # TODO "selecionado" para True (pois um item foi
            # TODO selecionado)
            if tecla == 'Return':
                self.__executar_acao()
                selecionado = True

            # TODO caso a tecla seja a seta para cima "Up" ou "w",
            # TODO decrementar "self._i_selecao".
            # ! Caso "self._i_selecao" seja menor que a quantidade de
            # ! opções, não decrementar ou reiniciar do final da lista.
            if tecla == 'Up' or tecla == 'W' or tecla == 'w' \
                    and self._i_selecao >= 0:
                self._i_selecao -= 1
                mudanca_de_opcao = True

            if self._i_selecao < 0:
                self._i_selecao = len(self._itens)-1
                mudanca_de_opcao = True

            # TODO caso a tecla seja a seta para baixo "Down" ou "s",
            # TODO incrementar "self._i_selecao".
            # ! Caso "self._i_selecao" seja maior que a quantidade de
            # ! opções, não incrementar ou reiniciar do início da lista.
            if tecla == 'Down' or tecla == 'S' or tecla == 's' \
                    and self._i_selecao < len(self._itens):
                self._i_selecao += 1
                mudanca_de_opcao = True

            if self._i_selecao > len(self._itens)-1:
                self._i_selecao = 0
                mudanca_de_opcao = True

            if mudanca_de_opcao:
                self.__apagar()
                self.__desenhar(janela)
                mudanca_de_opcao = False

        self.__apagar()

    def __desenhar(self, janela: GraphWin) -> None:
        """Desenha o menu na tela do jogo. Os itens do menu estão
        contidos no dicionário "self.itens".

        Args:
            janela (GraphWin): Janela na qual o programa está sendo
            executado.
        """
        # TODO Limpa a janela.
        self.__apagar()
        # TODO Desenha os itens do menu de opções de acordo com a lista
        # TODO "self._itens".
        # ! A opção selecionada "self._i_selecao" deve ser destacada.
        y = janela.height / 5
        for i in range(len(self._itens)):

            item = self._itens[i]
            self.texts.append(Text(Point(janela.width / 2, y), item))
            y += janela.height / 5

            if self._i_selecao == i:
                self.texts[-1].setSize(30)
                self.texts[-1].setFill('lime')
            else:
                self.texts[-1].setSize(25)
                self.texts[-1].setFill('black')

            self.texts[-1].draw(janela)

    def __executar_acao(self) -> None:
        """Executa a ação associada ao item selecionado (identificado
        pelo parâmetro "self._i_selecao").
        """
        # TODO Atualizar o valor do parâmetro "self.continuar" para
        # TODO True caso "self.itens" de "self._i_selecao" continuar
        if self._itens[self._i_selecao] == 'Continuar':
            self.continuar = True
        # TODO Atualizar o valor do parâmetro "self.iniciar" caso para
        # TODO True caso "self.itens" de "self._i_selecao" seja iniciar
        if self._itens[self._i_selecao] == 'Iniciar':
            self.iniciar = True
        # TODO Atualizar o valor do parâmetro "self.ranking" caso para
        # TODO True caso "self.itens" de "self._i_selecao" seja ranking
        if self._itens[self._i_selecao] == 'Ranking':
            self.ranking = True
        # TODO Atualizar o valor do parâmetro "self.sair" caso para
        # TODO True caso "self.itens" de "self._i_selecao" seja sair
        if self._itens[self._i_selecao] == 'Sair':
            self.sair = True

    def __apagar(self) -> None:
        for i in range(len(self.texts)):
            self.texts[i].undraw()
