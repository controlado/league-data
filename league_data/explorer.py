"""Explore e entenda facilmente os dados dos campeões.

GitHub:
    https://github.com/controlado/league-data

Discord:
    `Balaclava#1912`
    `854886148455399436`

Licença:
    `GNU` `Version 2`
"""


class Explorer:
    """Explore e entenda facilmente os dados dos campeões.

    Essa classe deve ser utilizada como apoio à classe League.

    Atributos:
        data (dict): Os dados crus extraídos da classe League.
        champions (dict): Os dados crus reformulados.
    """

    def __init__(self, data: dict) -> None:
        """Reformula os dados que recebe como parâmetro."""
        self.data = data
        self.champions = self.__get_champions()

    def get_item(self, name: str) -> dict | None:
        """Retorna os dados do item, caso exista.

        Args:
            name (str): Nome do item.

        Returns:
            dict | None: Dados do item requisitado.
        """
        name = name.lower()  # todos os champions estão como lower.

        if name in self.champions:
            return self.champions[name]

        for champion in self.champions:
            if name in self.champions[champion]["skins"]:
                return self.champions[champion]["skins"][name]

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

    @staticmethod
    def get_splash_art(champion_id: str, skin_id: str) -> str:
        """Retorna a URL do campeão ou da skin desejada com base em seus IDS."""
        return f"https://raw.communitydragon.org/latest/plugins/rcp-be-lol-game-data/global/default/v1/champion-splashes/{champion_id}/{skin_id}.jpg"
