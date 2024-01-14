# ROADMAP

Roadmap detalhado das tasks de cada fase

> 🟢 Concluído | 🟡 Em andamento | 🔴 Pendente

# Pré-processamento 
## Busca e criaçao do dataset:
- 🟢 Busca pelos PDFs de desempenho geral dos vestibulares
- 🟢 Busca pelos PDFs de relação candidato/vaga dos vestibulares
- 🟡 Criação do `course_info.csv`
    - 🟢 Extrair informações dos PDFs dos anos 2020, 2021, 2022
    - 🔴 Extrair informações dos PDFs do ano de 2019 (formato diferente)
- 🟢 Criaçao do `candidates_info.csv`  
## Processamento (Notebook 1)
- 🟢 Formatação das colunas
- 🟢 Criaçao do atributo `idade`
- 🟢 Formatação do atributo `id_curso_referencia`
- 🔴 Ordenar dataset de acordo com o PDF
    - 🔴 Agrupar por `ano`
    - 🔴 Agrupar por `curso_nome_referencia`
    - 🔴 Agrupar por `id_curso_referencia`
    - 🔴 Ordenar por `classificacao`
- 🔴 Criar atributo `passou`
- 🔴 Média de notas por idade
- 🔴 Média de aprovaçao por idade
- 🔴 Correlaçao de Pearson entre nota e idade (?)

> O atributo `passou` precisa ser gerado utilizando os datasets `course_info.csv` e `candidates_info.csv`, seguindo as regras estabelecida na sessão **PDF dos cursos** no README.md da pasta `src`. Os valores possíveis podem ser `0` (não) ou `1` (sim).

