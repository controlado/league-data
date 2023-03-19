# Início

Tenha os dados dos campeões e skins do League of Legends com facilidade.

- [Pypi](https://pypi.org/project/league-data/)
- [Documentação](https://league-data.readthedocs.io/en/latest/)
- [Releases](https://github.com/controlado/league-data/releases/)

## Dependências

Você só precisa do Python, qualquer dependência vai ser instalada automaticamente.

- [Python 3.11](https://www.python.org/downloads/release/python-3112/) (ou alguma outra superior)
- [Requests 2.28.2](https://requests.readthedocs.io/en/latest/) (é instalado automaticamente)

## Instalação

Basta executar esse comando no seu terminal.

    python -m pip install league-data


## Exemplos

<details>
    <summary> Buscar um campeão ou skin </summary>

    ```python linenums="1"
    from league_data import League

    league = League()
    champion = league["zeri"]  # -> <league_data.models.Champion object at ...>
    skin = league["ocean song zeri"]  # -> <league_data.models.Skin object at ...>
    skin.data  # todo objeto possui o seu dicionário de informações também
    ```

</details>

<details>
    <summary> Navegar nas informações dos itens </summary>

    ```python linenums="1" title="Existe duas sintaxes no projeto, utilizando objetos e dicionários."
    from league_data import League

    league = League()
    champion = league["zeri"]  # -> <league_data.models.Champion object at ...>
    skins_object = champion.skins  # -> [<league_data.models.Skin object>, ...]
    skins_dict = champion["skins"]  # -> {"nightblade irelia": {"id": ...}, ...}
    ```

</details>

<details>
    <summary> Reutilizar os dados antigos </summary>

    ```python linenums="1" title="Ao instanciar a classe League, é gerado os dados se não o receber no parâmetro."
    from league_data import League

    data = League.get_data()  # vai apenas resgatar os dados
    league = League(data=data)  # instanciando e reutilizando os dados
    champion = league["zeri"]  # -> <league_data.models.Champion object at ...>
    ```

</details>
