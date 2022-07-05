from graphics import GraphWin, Point, Text
import json


class Ranking:

    _dados: dict[str, int]
    _endereco_dados: str
    _rank: list[Text]

    def __init__(self, endereco_dados: str = "data\\ranking.json") -> None:
        self._endereco_dados = endereco_dados
        self._dados = {}
        self._rank = []

    def rodar(self, janela: GraphWin) -> None:
        """Roda o ranking do jogo.

        Args:
            janela (GraphWin): Janela na qual o programa está sendo
            executado.
        """
        # TODO carregar dados do ranking a partir do arquivo
        # TODO ranking.json da pasta dados "self.__carregar_dados"
        self.__carregar_dados()

        # TODO desenhar ranking chamando o método "self.__desenhar"
        self.__desenhar(janela)
        # Loop de leitura do ranking
        voltar = False
        while not voltar:
            # TODO ler tecla do jogador
            tecla = janela.checkKey()
            # TODO caso a tecla seja enter "Return", atualizar a
            # TODO variável "voltar" para True (pois o jogador deseja
            # TODO retornar ao menu principal)
            if tecla == 'Return':
                self.__apagar()
                voltar = True

    def __carregar_dados(self) -> None:
        """Lê os dados do ranking que estão contidos num arquivo json.
        O arquivo json se encontra no endereço do parâmetro
        "self.endereco_dados". Os dados são armazenados no dicionário
        "self._dados".
        """
        # TODO abrir arquivo json em "self.endereco_dados" em modo
        # TODO leitura e armazenar seu conteúdo no dicionário
        # TODO "self._dados".
        with open('data\\ranking.json', 'r') as data:
            self._dados = json.load(data)

    def __desenhar(self, janela: GraphWin) -> None:
        """Desenha o ranking na janela do jogo.

        Args:
            janela (GraphWin): Janela na qual o programa está sendo
            executado.
        """
        # TODO Limpa a janela.

        # TODO Ordena e desenha a lista do ranking. Desenhar nomes e
        # TODO quantidades de partidas ganhas.
        ordem = sorted(self._dados, key=self._dados.get, reverse=True)
        y = janela.height / 10
        for v in ordem:
            self._rank.append(Text(Point(janela.width / 2, y), '{}: {}'.format(v, self._dados[v])))
            y += 50
            self._rank[-1].setSize(20)
            self._rank[-1].draw(janela)
        pass

    def atualizar_dados(self, nome_jogador: str) -> None:
        """Atualiza o arquivo json do ranking para atribuir uma nova
        vitória ao nome de jogador especificado.

        Args:
            nome_jogador (str): Nome do jogador cujo número de partidas
            ganhas será incrementado.
        """
        # TODO Chamar o método self.__carregar_dados
        self.__carregar_dados()
        # TODO Modificar "self._dados" para registrar a nova vitória do
        # TODO jogador.
        if nome_jogador not in self._dados.keys():
            self._dados[nome_jogador] = 0
        self._dados[nome_jogador] += 1
        # TODO Abrir o arquivo json em modo escrita e reescrever seu conteúdo
        # TODO de acordo com os dados atualizados.
        with open('data\\ranking.json', 'w') as jsonfile:
            json.dump(self._dados, jsonfile)

    def __apagar(self) -> None:
        for i in range(len(self._rank)):
            self._rank[i].undraw()
