from graphics import GraphWin


class Ranking:

    _dados: dict[str, int]
    _endereco_dados: str

    def __init__(self, endereco_dados: str = "data\\ranking.json") -> None:
        self._endereco_dados = endereco_dados
        self._dados = {}

    def rodar(self, janela: GraphWin) -> None:
        """Roda o ranking do jogo.

        Args:
            janela (GraphWin): Janela na qual o programa está sendo
            executado.
        """
        # TODO carregar dados do ranking a partir do arquivo
        # TODO ranking.json da pasta dados "self.__carregar_dados"

        # TODO desenhar ranking chamando o método "self.__desenhar"

        # Loop de leitura do ranking
        voltar = False
        while not voltar:
            # TODO ler tecla do jogador

            # TODO caso a tecla seja enter "Return", atualizar a
            # TODO variável "voltar" para True (pois o jogador deseja
            # TODO retornar ao menu principal)
            break

        pass

    def __carregar_dados(self) -> None:
        """Lê os dados do ranking que estão contidos num arquivo json.
        O arquivo json se encontra no endereço do parâmetro
        "self.endereco_dados". Os dados são armazenados no dicionário
        "self._dados".
        """
        # TODO abrir arquivo json em "self.endereco_dados" em modo
        # TODO leitura e armazenar seu conteúdo no dicionário
        # TODO "self._dados".
        pass

    def __desenhar(self, janela: GraphWin) -> None:
        """Desenha o ranking na janela do jogo.

        Args:
            janela (GraphWin): Janela na qual o programa está sendo
            executado.
        """
        # TODO Limpa a janela.

        # TODO Ordena e desenha a lista do ranking. Desenhar nomes e
        # TODO quantidades de partidas ganhas.
        pass

    def atualizar_dados(self, nome_jogador: str) -> None:
        """Atualiza o arquivo json do ranking para atribuir uma nova
        vitória ao nome de jogador especificado.

        Args:
            nome_jogador (str): Nome do jogador cujo número de partidas
            ganhas será incrementado.
        """
        # TODO Chamar o método self.__carregar_dados

        # TODO Modificar "self._dados" para registrar a nova vitória do
        # TODO jogador.

        # TODO Abrir o arquivo json em modo escrita e reescrever seu conteúdo
        # TODO de acordo com os dados atualizados.
        pass
