# `📩` League-data

Tenha os dados dos campeões e skins do League of Legends com facilidade.

- [Documentação](https://league-data.readthedocs.io/en/latest/)
- [Pypi](https://pypi.org/project/league-data/)
- [Releases](https://github.com/controlado/league-data/releases/)

## Dependências

- [Python 3.11](https://www.python.org/downloads/release/python-3112/) (ou alguma outra superior)
- [Requests 2.28.2](https://requests.readthedocs.io/en/latest/) (é instalado automaticamente)

Com o Python instalado, basta seguir as etapas de instalação.

## Instalação

```
pip install league-data
```

## Exemplos

<details>
    <summary> Buscar um campeão ou skin </summary>

```python
from league_data import League

league = League()
champion = league["zeri"]  # -> <league_data.models.Champion object at ...>
skin = league["ocean song zeri"]  # -> <league_data.models.Skin object at ...>
skin.data  # todo objeto possui o seu dicionário de informações também
```

</details>

<details>
    <summary> Navegar nas informações dos itens </summary>
    Existe duas sintaxes no projeto, utilizando objetos e dicionários.

```python
from league_data import League

league = League()
champion = league["zeri"]  # -> <league_data.models.Champion object at ...>
skins_object = champion.skins  # -> [<league_data.models.Skin object>, ...]
skins_dict = champion["skins"]  # -> {"nightblade irelia": {"id": ...}, ...}
```

</details>

<details>
    <summary> Reutilizar os dados antigos </summary>
    Ao instanciar a classe League, é gerado os dados se não o receber no parâmetro.

```python
from league_data import League

data = League.get_data()  # vai apenas resgatar os dados
league = League(data=data)  # instanciando e reutilizando os dados
champion = league["zeri"]  # -> <league_data.models.Champion object at ...>
```

</details>
