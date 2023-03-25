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

    @property
    def skins(self) -> list[Skin]:
        """Skins que o campeão possui."""
        return self.get_skins()

    def get_skins(self) -> list[Skin]:
        """Cria uma lista com as skins do campeão.

        O método faz o processo com list comprehension.

        Returns:
            list[Skin]: Lista com as skins.
        """
        return [
            Skin(
                explorer=self.explorer,
                champion=self.data,
                data=self.data["skins"][skin],
            )
            for skin in self.data["skins"]
        ]

    def __init__(self, explorer: Explorer, data: dict) -> None:
        """Instancia o objeto contendo as informações do campeão.

        Args:
            explorer (Explorer): Explorador que buscou esse campeão.
            data (dict): Os dados desse campeão.
        """
        self.explorer = explorer
        self.data = data
        self.identity: str = self.data["id"]
        self.name: str = self.data["name"]
        self.art: str = self.data["art"]

    def __getitem__(self, value: str) -> Any:
        """Retorna um valor do dicionário do campeão."""
        return self.data.get(value)

    def __str__(self) -> str:
        """Forma string da classe."""
        return self.name

    def __repr__(self) -> str:
        """Representa a forma que a instância foi criada."""
        return f"Champion({self.explorer, self.data})"


class Skin:
    """Objeto que contém as informações de uma skin.

    Attributes:
        explorer (Explorer): Explorador que buscou essa skin.
        data (dict): Os dados dessa skin.
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

    @property
    def champion(self) -> Champion:
        """O campeão que possui essa skin."""
        return Champion(self.explorer, self._champion)

    def __init__(self, explorer: Explorer, champion: dict, data: dict) -> None:
        """Instancia o objeto contendo as informações da skin.

        Args:
            explorer (Explorer): Explorador que buscou essa skin.
            champion (dict): Dados do campeão que possui essa skin.
            data (dict): Os dados dessa skin.
        """
        self.explorer = explorer
        self._champion = champion
        self.data = data
        self.identity: str = self.data["id"]
        self.name: str = self.data["name"]
        self.art: str = self.data["art"]
        self.rarity: str = self.data["rarity"]

    def __getitem__(self, value: str) -> Any:
        """Retorna um valor do dicionário da skin."""
        return self.data.get(value)

    def __str__(self) -> str:
        """Forma string da classe."""
        return self.name

    def __repr__(self) -> str:
        """Representa a forma que a instância foi criada."""
        return f"Skin({self.explorer}, {self.champion.data}, {self.data})"
