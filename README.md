# `📩` League-data

Tenha os dados dos campeões e skins do League of Legends com facilidade.

- [Documentação](https://league-data.readthedocs.io/en/latest/)
- [Pypi](https://pypi.org/project/league-data/)
- [Releases](https://github.com/controlado/league-data/releases/)

## Dependências

- [Python 3.11](https://www.python.org/downloads/release/python-3112/) (ou alguma outra superior)
- [Requests 2.28.2](https://requests.readthedocs.io/en/latest/) (é instalado automaticamente)

## Instalação

Com o Python instalado, basta executar esse comando no seu terminal.

```
pip install league-data
```

## Exemplos

Clique [aqui](https://league-data.readthedocs.io/en/latest/#exemplos) para ver outros exemplos na documentação.

```python
from league_data import League

league = League()
champion = league["zeri"]  # -> <league_data.models.Champion object at ...>
skin = league["ocean song zeri"]  # -> <league_data.models.Skin object at ...>
```
