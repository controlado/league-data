"""Tenha acesso facilmente aos dados dos campeões e skins do League of Legends.

GitHub:
    https://github.com/controlado/league-data

Discord:
    `Balaclava#1912`
    `854886148455399436`

Licença:
    `GNU` `Version 2`
"""

from requests import Timeout, request

from league_data import Explorer
from league_data.models import Champion, Skin


class League:
    """Tenha acesso facilmente aos dados dos campeões e skins do League of Legends.

    Attributes:
        data (dict): Dados da Riot.
        explorer (Explorer): Explorador de dados.
        champions (dict): Dicionário de campeões.
    """

    def update(self) -> None:
        """Atualiza os dados e recria o dicionário de campeões.

        Example:
            ```python linenums="1"
            from league_data import League

            league = League()
            milio = league["milio"]  # -> None
            league.update()  # atualizando os dados e os campeões
            milio = league["milio"]  # -> <league_data.models.Champion object at ...>
            ```
        """
        self.data = self.get_data()
        self.explorer = Explorer(self.data)
        self.champions = self.explorer.champions

    @staticmethod
    def get_data() -> dict:
        """Busca todos os dados dos campeões do League of Legends.

        Uma requisição é feita para conseguir esses dados.

        Raises:
            ConnectionError: Caso não consiga realizar a requisição.

        Returns:
            data (dict): Os dados dos campeões e suas skins.

        Example:
            ```python linenums="1" title="Não é necessário instanciar a classe."
            from league_data import League

            data = League.get_data()  # -> {"1000": {"id": 1000, "isBase": ...}, ...}
            ```
        """
        url = "https://raw.communitydragon.org/latest/plugins/rcp-be-lol-game-data/global/default/v1/skins.json"

        try:
            response = request(method="get", url=url, timeout=10)
        except Timeout as exception:
            message = "A request demorou muito para ser finalizada..."
            raise ConnectionError(message) from exception

        return response.json()

    def __init__(self, data: dict | None = None, champions: dict | None = None) -> None:
        """Cria o um explorador automaticamente para a instância.

        Caso não receba os parâmetros, serão requisitados automaticamente.

        Args:
            data (dict, optional): Dados da Riot, gerados pelo League.
            champions (dict, optional): Dicionário de campeões, gerados pelo Explorer.
        """
        self.data = data or self.get_data()
        self.explorer = Explorer(self.data, champions)
        self.champions = self.explorer.champions

    def __getitem__(self, name: str) -> Champion | Skin | None:
        """Retorna os dados do campeão ou skin, caso exista.

        Args:
            name (str): Nome do campeão ou skin.

        Returns:
            Champion (Champion): Objeto do campeão encontrado.
            Skin (Skin): Objeto da skin encontrada.
            None (None): Nenhum item foi encontrado.
        """
        return self.explorer[name]
