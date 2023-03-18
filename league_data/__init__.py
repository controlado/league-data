"""Tenha acesso facilmente aos dados dos campeões e skins do League of Legends.

Para utilizar o módulo, importe a classe League e crie uma instância da mesma,
logo em seguida, simplesmente busque um campeão ou skin como se fosse um dict.

Exemplo:
    ```python
    from league_data import League

    league = League()  # instancia a classe corretamente
    zeri_data = league["zeri"]  # retorna os dados da campeã
    zeri_skin = league["ocean song zeri"]  # retorna os dados da skin
    wrong_way = league["bla-bla-bla"]  # sendo inválido, retorna None
    ```

GitHub:
    https://github.com/controlado/league-data

Discord:
    `Balaclava#1912`
    `854886148455399436`

Licença:
    `GNU` `Version 2`
"""

from league_data.explorer import Explorer
from league_data.league import League
