<div align="center">

  # `🌍` League-data <br> [![Documentação](https://readthedocs.org/projects/league-data/badge/?version=latest)](https://league-data.readthedocs.io/en/latest/?badge=latest) [![Versão](https://img.shields.io/pypi/v/league-data?color=blue)](https://pypi.org/project/league-data/) [![Wakatime](https://wakatime.com/badge/user/89c5e1c8-9e67-43ef-bd0e-3ff9a4fde5e2/project/8e653575-2e7d-4774-806b-b42826f8b005.svg)](https://wakatime.com/badge/user/89c5e1c8-9e67-43ef-bd0e-3ff9a4fde5e2/project/8e653575-2e7d-4774-806b-b42826f8b005) <br> [![Estilo: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) [![Linting: pylint](https://img.shields.io/badge/linting-pylint-black)](https://github.com/PyCQA/pylint) [![Imports: isort](https://img.shields.io/badge/imports-isort-black?style=flat)](https://pycqa.github.io/isort/)

  Campeões e skins do League of Legends com facilidade.

</div>
<br>

## Dependências
[Python 3.11](https://www.python.org/downloads/release/python-3112/) (ou qualquer versão superior) <br>
[Requests](https://requests.readthedocs.io/en/latest/) (instalado automaticamente, se necessário)

## Instalação
Execute o comando abaixo em seu terminal.

    python -m pip install league-data

## Como funciona?
A biblioteca foi criada para facilitar a vida de pessoas que usam dados do League of Legends. <br>
Você pode, por exemplo, buscar as skins de cada campeão de forma atualizada e automática!

### Exemplos
<details>
  <summary> Clique para visualizar o <b> código de exemplo </b> </summary>
  <br>

  ```python
  from league_data import League

  league = League()
  champion = league["zeri"]  # -> <league_data.models.Champion object at ...>
  skin = league["ocean song zeri"]  # -> <league_data.models.Skin object at ...>
  ```

</details>
<details>
  <summary> Clique para visualizar um <b> vídeo de demonstração </b> </summary>
  <br>

  https://user-images.githubusercontent.com/71716568/226250489-f9845f28-c870-4b34-b762-bae7e0a7ab19.mp4

</details>

[Outros exemplos](https://league-data.readthedocs.io/en/latest/#exemplos) estão disponíveis na [documentação](https://league-data.readthedocs.io/en/latest/).
