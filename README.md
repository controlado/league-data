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

<details>
    <summary> Buscar um campeão ou skin </summary>

```python
    from league_data import League

    league = League()
    champion = league["zeri"]  # vai retornar um objeto (<league_data.models.Champion object at ...>)
    skin = league["ocean song zeri"]  # vai retornar um objeto (<league_data.models.Skin object at ...>)
    skin_data = skin.data  # todo objeto possui o seu dicionário de informações também
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
