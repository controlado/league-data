# 🌍 League-data

Campeões e skins do League of Legends com facilidade.

[![Documentação](https://readthedocs.org/projects/league-data/badge/?version=latest)](https://league-data.readthedocs.io/en/latest/?badge=latest)
[![Versão](https://img.shields.io/pypi/v/league-data?color=blue)](https://pypi.org/project/league-data/)
[![Imports: isort](https://img.shields.io/badge/imports-isort-%231674b1?style=flat)](https://pycqa.github.io/isort/)
[![Estilo: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Dependências

Você só precisa do Python, qualquer dependência adicional vai ser instalada automaticamente.

- [Python 3.11](https://www.python.org/downloads/release/python-3112/) (ou alguma outra superior)
- [Requests 2.28.2](https://requests.readthedocs.io/en/latest/) (é instalado automaticamente)

## Instalação

Basta executar esse comando no seu terminal.

    python -m pip install league-data

## Como funciona?

A biblioteca foi criada para facilitar a vida de quem usa os dados de campeões do League of Legends.

### Exemplos

<details>
    <summary> Clique para visualizar o código de exemplo </summary> </br>
    
```python
from league_data import League

league = League()
champion = league["zeri"]  # -> <league_data.models.Champion object at ...>
skin = league["ocean song zeri"]  # -> <league_data.models.Skin object at ...>
```

</details>

[Outros exemplos](https://league-data.readthedocs.io/en/latest/#exemplos) estão disponíveis na [documentação](https://league-data.readthedocs.io/en/latest/).
