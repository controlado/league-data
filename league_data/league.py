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

from league_data.explorer import Explorer
from league_data.models import Champion, Skin


class League:
    """Tenha acesso facilmente aos dados dos campeões e skins do League of Legends."""

    @staticmethod
    def get_data() -> dict:
        """Busca todos os dados dos campeões do League of Legends.

        Uma requisição é feita para conseguir esses dados.

        Raises:
            ConnectionError: Caso não consiga realizar a requisição.

        Returns:
            data (dict): Os dados dos campeões e suas skins.
        """
        url = "https://raw.communitydragon.org/latest/plugins/rcp-be-lol-game-data/global/default/v1/skins.json"

        try:
            response = request(method="get", url=url, timeout=10)
        except Timeout as exception:
            message = "A request demorou muito para ser finalizada..."
            raise ConnectionError(message) from exception

        return response.json()

    def __init__(self, data: dict = None) -> None:
        """Cria o um explorador automaticamente para a instância.

        Caso não receba o parâmetro data, o mesmo será requisitado automaticamente.

        Args:
            data (dict, optional): Dados da Riot.
        """
        self.data = data or self.get_data()
        self.explorer = Explorer(self.data)

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
