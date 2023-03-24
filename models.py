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

from dataclasses import dataclass, field
from typing import Any

import league_data


@dataclass
class Champion:
    """Objeto que contém as informações de um campeão.

    Parameters:
        explorer (Explorer): Explorador que buscou esse campeão.
        data (dict): Os dados crus desse campeão.

    Attributes:
        identity (str): ID do campeão.
        name (str): Nome do campeão.
        art (str): URL da arte do campeão.

    Example:
        ```python linenums="1"
        from league_data import League

        league = League()
        irelia = league["irelia"]  # -> <league_data.models.Champion object at ...>
        ```
    """

    explorer: league_data.Explorer
    data: dict

    identity: str = field(init=False)
    name: str = field(init=False)
    art: str = field(init=False)

    @property
    def skins(self) -> list[Skin]:
        """Skins que o campeão possui."""
        return [
            Skin(
                explorer=self.explorer,
                champion_data=self.data,
                data=self.data["skins"][skin],
            )
            for skin in self.data["skins"]
        ]

    def __post_init__(self) -> None:
        """Método utilizado para definir os atributos."""
        self.identity = self.data["id"]
        self.name = self.data["name"]
        self.art = self.data["art"]

    def __getitem__(self, value: str) -> Any:
        """Retorna um valor do dicionário do campeão."""
        return self.data.get(value)

    def __str__(self) -> str:
        """Forma string da classe."""
        return self.name


@dataclass
class Skin:
    """Objeto que contém as informações de uma skin.

    Parameters:
        explorer (Explorer): Explorador que buscou essa skin.
        champion_data (dict): Dados do campeão que possui essa skin.
        data (dict): Os dados crus dessa skin.

    Attributes:
        identity (str): ID da skin.
        name (str): Nome da skin.
        art (str): URL da arte da skin.
        rarity (str): Raridade da skin.

    Example:
        ```python linenums="1"
        from league_data import League

        league = League()
        vayne = league["vayne"]
        vayne_skins = vayne.skins  # -> [<league_data.models.Skin object>, ...]
        vayne_skins = vayne["skins"]  # -> {"aristocrat vayne": {"id": ...}, ...}
        ```
    """

    explorer: league_data.Explorer
    champion_data: dict
    data: dict

    identity: str = field(init=False)
    name: str = field(init=False)
    art: str = field(init=False)
    rarity: str = field(init=False)

    @property
    def champion(self) -> Champion:
        """O campeão que possui essa skin."""
        return Champion(self.explorer, self.champion_data)

    def __post_init__(self) -> None:
        """Método utilizado para definir os atributos."""
        self.identity = self.data["id"]
        self.name = self.data["name"]
        self.art = self.data["art"]
        self.rarity = self.data["rarity"]

    def __getitem__(self, value: str) -> Any:
        """Retorna um valor do dicionário da skin."""
        return self.data.get(value)

    def __str__(self) -> str:
        """Forma string da classe."""
        return self.name
