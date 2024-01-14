# Análise de Candidatos ao Vestibular da UEA
UEA — Universidade do Estado do Amazonas \
**Curso:** Sistemas de Informação \
**Matéria:** Mineração de Dados 
## Sumário

- [Como instalar](#como-instalar)
- [Roadmap](#roadmap)
  - [Extração de dados](#extração-dos-dados)
  - [Pré-processamento dos dados](#pré-processamento-dos-dados)
  - [Exploração](#exploração)
  - [Treinamento](#treinamento)
- [Autores](#autores)

## Como Instalar

### Requisitos

Ter instalado:

- Python 3.10.5
- VSCode (Visual Studio Code)

### Windows

No Powershell, execute os seguintes passos (na raiz do projeto):

```shell
# configure project (create and change env, install dependencies)
.\configure.ps1
```

Agora você está apto a editar o arquivo [`main.ipynb`](./main.ipynb).

> Não se esqueça de alterar o ambiente virtual para o ambiente local que acabou de ser configurado. [Clique aqui para saber mais.](https://code.visualstudio.com/docs/python/environments)

> [Jupyter Notebook no VSCode](https://code.visualstudio.com/docs/datascience/jupyter-notebooks)

### Geração de CSV

Caso queira gerar os arquivos csv da pasta `/data/csv/` novamente, execute o seguinto comando na raíz do projeto:

```shell
.\venv\Scripts\python generator.py
```

## Roadmap

> 🟢 Concluído | 🟡 Em andamento | 🔴 Não iniciado

#### Extração dos dados

- 🟢 Busca dos dados brutos (vestibulares 2019-2022)
- 🟢 Converter dados para um CSV

#### Pré-processamento dos dados

- 🟢 Avaliação de qualidade dos dados
- 🟡 Preparação de dados
- 🟡 Preparação de dados (limpar dados)
- 🟡 Preparação de dados (padronização)
- 🟡 Preparação de dados (discretização)
- 🟡 Preparação de dados (geração de novos atributos)
- 🟡 Tratar dados com ética (LGPD)

#### Exploração

- 🔴 Tratar outliers
- 🔴 Seleção de características relevantes

#### Treinamento

- 🔴 Réplica do estado da arte do contexto
- 🔴 Aplicação de algoritmo supervisionado (ao - 2)
- 🔴 Gerar modelo para a previsão
- 🔴 Gerar modelo para determinar risco e probabilidade (?)
- 🔴 Gerar modelo para localizar sequências de ações de cliente/usuário (?)
- 🔴 Aplicação de medidas de similaridade e/ou dissimilaridade para o problema

## Autores

- Gabriel dos Santos Lima
- Melinne Diniz de Oliveira
- Lídia Dias de Souza
