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

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:  # apenas para tipagem estática
    from league_data.explorer import Explorer


class Champion:
    """Objeto que contém as informações de um campeão.

    Attributes:
        explorer (Explorer): Explorador que buscou esse campeão.
        data (dict): Os dados desse campeão.

    Example:
        ```python linenums="1"
        from league_data import League

        league = League()
        irelia = league["irelia"]  # -> <league_data.models.Champion object at ...>
        ```
    """

    def __init__(self, explorer: Explorer, data: dict) -> None:
        """Instancia o objeto contendo as informações do campeão.

        Args:
            explorer (Explorer): Explorador que buscou esse campeão.
            data (dict): Os dados desse campeão.
        """
        self.explorer = explorer
        self.data = data

    def __getitem__(self, value: str) -> Any:
        """Retorna um valor do dicionário do campeão."""
        return self.data.get(value)

    def __str__(self) -> str:
        """Forma string da classe."""
        return self.name

    @property
    def identity(self) -> str:
        """ID do campeão."""
        return self.data["id"]

    @property
    def name(self) -> str:
        """Nome do campeão."""
        return self.data["name"]

    @property
    def art(self) -> str:
        """URL da arte do campeão."""
        return self.data["art"]

    @property
    def skins(self) -> list[Skin]:
        """Skins que o campeão possui."""
        return [
            Skin(
                explorer=self.explorer,
                champion=self.data,
                data=self.data["skins"][skin],
            )
            for skin in self.data["skins"]
        ]


class Skin:
    """Objeto que contém as informações de uma skin.

    Attributes:
        explorer (Explorer): Explorador que buscou essa skin.
        champion_data (dict): Dados do campeão que possui essa skin.
        data (dict): Os dados dessa skin.

    Example:
        ```python linenums="1"
        from league_data import League

        league = League()
        vayne = league["vayne"]
        vayne_skins = vayne.skins  # -> [<league_data.models.Skin object>, ...]
        vayne_skins = vayne["skins"]  # -> {"aristocrat vayne": {"id": ...}, ...}
        ```
    """

    def __init__(self, explorer: Explorer, champion: dict, data: dict) -> None:
        """Instancia o objeto contendo as informações da skin.

        Args:
            explorer (Explorer): Explorador que buscou essa skin.
            champion (dict): Dados do campeão que possui essa skin.
            data (dict): Os dados dessa skin.
        """
        self.explorer = explorer
        self.champion_data = champion
        self.data = data

    def __getitem__(self, value: str) -> Any:
        """Retorna um valor do dicionário da skin."""
        return self.data.get(value)

    def __str__(self) -> str:
        """Forma string da classe."""
        return self.name

    @property
    def identity(self) -> str:
        """ID da skin."""
        return self.data["id"]

    @property
    def name(self) -> str:
        """Nome da skin."""
        return self.data["name"]

    @property
    def art(self) -> str:
        """URL da arte da skin."""
        return self.data["art"]

    @property
    def rarity(self) -> str:
        """Raridade da skin."""
        return self.data["rarity"]

    @property
    def champion(self) -> Champion:
        """O campeão que possui essa skin."""
        return Champion(self.explorer, self.champion_data)
