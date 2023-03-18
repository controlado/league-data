"""Explore e entenda facilmente os dados dos campeões.

GitHub:
    https://github.com/controlado/league-data

Discord:
    `Balaclava#1912`
    `854886148455399436`

Licença:
    `GNU` `Version 2`
"""

from league_data.models import Champion, Skin


class Explorer:
    """Explore e entenda facilmente os dados dos campeões."""

    def get_champion(self, name: str) -> Champion | None:
        """Retorna o objeto do campeão, caso exista.

        Args:
            name (str): Nome do campeão.

        Returns:
            Champion (Champion): O objeto que contém os dados do campeão.
            None (None): Caso o nome do campeão não seja válido.
        """
        name = name.lower()

        if name in self.champions:
            champion_data = self.champions[name]
            return Champion(self, champion_data)

    def get_skin(self, name: str) -> Skin | None:
        """Retorna o objeto da skin, caso exista.

        Args:
            name (str): Nome da skin.

        Returns:
            Skin (Skin): O objeto que contém os dados da skin.
            None (None): Caso o nome da skin não seja válida.
        """
        name = name.lower()

        for champion in self.champions:
            if name in self.champions[champion]["skins"]:
                champion_data = self.champions[champion]
                skin_data = self.champions[champion]["skins"][name]
                return Skin(self, champion_data, skin_data)

    @staticmethod
    def get_splash_art(champion_id: str, skin_id: str) -> str:
        """Retorna a URL do campeão ou da skin desejada com base em seus IDS."""
        return f"https://raw.communitydragon.org/latest/plugins/rcp-be-lol-game-data/global/default/v1/champion-splashes/{champion_id}/{skin_id}.jpg"

    def __init__(self, data: dict) -> None:
        """Reformula os dados que recebe como parâmetro."""
        self.data = data
        self.champions = self.__get_champions()

    def __getitem__(self, name: str) -> Champion | Skin | None:
        """Retorna os dados do campeão ou skin, caso exista.

        Args:
            name (str): Nome do campeão ou skin.

        Returns:
            Champion (Champion): Objeto do campeão encontrado.
            Skin (Skin): Objeto da skin encontrada.
            None (None): Nenhum item foi encontrado.
        """
        if champion := self.get_champion(name):
            return champion

        return self.get_skin(name)

    def __get_champions(self) -> dict:
        champions = {}

        for index in self.data:
            if not self.data[index]["isBase"]:
                continue

            champion_name = self.data[index]["name"]
            champion_id = self.__get_champion_id(index)
            champions[champion_name.lower()] = {
                "id": champion_id,
                "name": champion_name,
                "art": self.get_splash_art(champion_id, index),
                "skins": self.__get_champion_skins(champion_id)
            }

        return champions

    def __get_champion_skins(self, champion_id: str) -> dict:
        skins = {}

        for index in self.data:
            if self.data[index]["isBase"]:
                continue

            if self.__get_champion_id(index) != champion_id:
                continue  # apenas as skins do campeão solicitado.

            skin_name = self.data[index]["name"]
            skins[skin_name.lower()] = {
                "id": index,
                "name": skin_name,
                "rarity": self.data[index]["rarity"],
                "art": self.get_splash_art(champion_id, index)
            }

        return skins

    def __get_champion_id(self, index: str) -> str:
        endpoint = self.data[index]["splashPath"]
        return endpoint.split("/")[-2]
