"""Modelos e objetos que contém os dados dos campeões e skins.

GitHub:
    https://github.com/controlado/league-data

Discord:
    `Balaclava#1912`
    `854886148455399436`

Licença:
    `GNU` `Version 2`
"""

from __future__ import annotations

from typing import Any


class Champion:
    """Objeto que contém as informações de um campeão.

    Atributos:
        explorer (Explorer): Explorador que criou este campeão.
        data (dict): Dicionário com as informações desse campeão.
    """

    def __init__(self, explorer: ..., data: dict) -> None:
        """Instancia o objeto contendo as informações do campeão.

        Exemplo de uso:
            ```python
            from league_data import League

            league = League()
            irelia = league["irelia"]

            skins = irelia.skins  # vai retornar uma lista com os objetos das skins
            skins = irelia/"skins"  # vai retornar as skins através de dicionários
            ```
        """
        self.explorer = explorer
        self.data = data

    def __truediv__(self, value: str) -> Any:
        """Retorna um valor do dicionário do campeão."""
        return self.data.get(value)

    def __str__(self) -> str:
        """Forma string da classe."""
        return self.name

    @property
    def skins(self) -> list[Skin]:
        """Retorna os objetos das skins do campeão."""
        return [
            Skin(
                self.explorer,
                self.data,
                self.data["skins"][data]
            )
            for data in self.data["skins"]
        ]

    @property
    def id(self) -> str:
        """Retorna o ID do campeão."""
        return self.data["id"]

    @property
    def name(self) -> str:
        """Retorna o nome do campeão."""
        return self.data["name"]

    @property
    def art(self) -> str:
        """Retorna a arte do campeão."""
        return self.data["art"]


class Skin:
    """Objeto que contém as informações de uma skin.

    Atributos:
        explorer (Explorer): Explorador que criou essa skin.
        champion (dict): Dicionário do campeão que possui essa skin.
        data (dict): Dicionário com as informações dessa skin.
    """

    def __init__(self, explorer: ..., champion: dict, data: dict) -> None:
        """Instancia o objeto contendo as informações da skin.

        Exemplo de uso:
            ```python
            from league_data import League

            league = League()
            vayne = league["vayne"]

            art = vayne.art  # vai retornar uma propriedade do objeto
            art = vayne/"art"  # vai retornar um item do dicionário da skin
            ```
        """
        self.explorer = explorer
        self.champion_data = champion
        self.data = data

    def __truediv__(self, value: str) -> Any:
        """Retorna um valor do dicionário da skin."""
        return self.data.get(value)

    def __str__(self) -> str:
        """Forma string da classe."""
        return self.name

    @property
    def champion(self) -> Champion:
        """Retorna o campeão que possui essa skin."""
        return Champion(self.explorer, self.champion_data)

    @property
    def id(self) -> str:
        """Retorna o ID da skin."""
        return self.data["id"]

    @property
    def name(self) -> str:
        """Retorna o nome da skin."""
        return self.data["name"]

    @property
    def rarity(self) -> str:
        """Retorna a raridade da skin."""
        return self.data["rarity"]

    @property
    def art(self) -> str:
        """Retorna a arte da skin."""
        return self.data["art"]
