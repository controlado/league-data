"""Tenha acesso facilmente aos dados dos campeões e skins do League of Legends.

GitHub:
    https://github.com/controlado/league-data

Discord:
    `Balaclava#1912`
    `854886148455399436`

Licença:
    `GNU` `Version 2`
"""

import requests

from league_data.explorer import Explorer
from league_data.models import Champion, Skin


class League:
    """Tenha acesso facilmente aos dados dos campeões e skins do League of Legends.

    Atributos:
        session (requests.Session): Sessão padrão para fazer qualquer requisição.
        data (dict): Os dados dos campeões de forma crua, não é destinado ao usuário.
        explorer (Explorer): Explorador dos dados crus para o usuário.
    """

    URL = "https://raw.communitydragon.org"

    def __init__(self) -> None:
        """Cria uma sessão e gera os dados necessários."""
        self.session = requests.Session()
        self.data = self.get_data()
        self.explorer = Explorer(self.data)

    def __getitem__(self, name: str) -> Champion | Skin | None:
        """Retorna os dados do campeão ou skin, caso exista.

        Args:
            name (str): Nome do campeão ou skin.

        Returns:
            Champion: Objeto do campeão encontrado.
            Skin: Objeto da skin encontrada.
            None: Nenhum item foi encontrado.
        """
        if champion := self.explorer.get_champion(name):
            return champion

        return self.explorer.get_skin(name)

    def get_data(self) -> dict:
        """Busca todos os dados dos campeões do League of Legends.

        Retorna:
            dict: Os dados dos campeões e suas skins.
        """
        url = f"{self.URL}/latest/plugins/rcp-be-lol-game-data/global/default/v1/skins.json"
        response = self.session.request(method="get", url=url)
        return response.json()
