# `📩` League-data

Tenha os dados dos campeões e skins do League of Legends com facilidade.

## Dependências

- [Python 3.11](https://www.python.org/downloads/release/python-3112/) (ou alguma outra superior)
- [Requests 2.28.2](https://requests.readthedocs.io/en/latest/) (é instalado automaticamente)

Com o Python instalado, basta seguir as etapas de instalação.

## Instalação

```
pip install league-data
```

## Exemplo de uso

```python
from league_data import League

league = League()
zeri_data = league["zeri"]
zeri_skin = league["ocean song zeri"]
```
