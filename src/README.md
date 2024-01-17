# Observações sobre a leitura dos PDFs

Conteúdo:
- [PDF dos candidatos](#pdf-dos-candidatos)
    - [Diferença entre páginas](#diferenças-entre-páginas)
        - [Vestibular 2019: ``data1``, pg. 1](#ordem-dos-itens-da-tabela-na-página-1-do-arquivo-data1pdf)
        - [Vestibular 2019: ``data1``, pg. 166](#ordem-dos-itens-na-página-166)
        - [Vestibular 2019: ``data2``, pg. 124](#ordem-dos-itens-na-página-124)
    - [Considerações](#considerações)
        - [Ordem da lista usada no CSV](#ordem-da-lista-retornada-da-função-extract_info)
- [PDF dos cursos](#pdf-dos-cursos)

# PDF dos candidatos
As páginas possuem algumas inconsistências, o que pode dificultar a extração de informação. Os principais problemas são:
- Em algumas páginas os candidatos escolhem somente uma opção (Opção 1) e em outras escolhem duas (Opção 1, Opção 2) ou três (Opção 1, Opção 2, Opção 3)
- Em algumas páginas os candidatos do curso de Teatro possuem a coluna Habilidade (mas é difícil saber em qual ordem é lido pela biblioteca)
- A extração da tabela não segue a mesma ordem do PDF

## Diferenças entre páginas
As diferenças foram observadas utilizando os arquivos `data/candidatos/data1.pdf` e `data/candidatos/data2.pdf` do vestibular de 2019.

### > *Ordem dos itens da tabela na  **página 1** do arquivo* `data1.pdf`
A página 1 possui todos os candidatos sem a **Opção 2** e **Opção 3** preenchida. 

Exemplo extraído com a função `extract_info()`:

`['6354130-0', 'EDIJANE PINHEIRO MARTINS', '04/03/92', '313', '31,161', '19,048', '19,048', '3', '5', '6', '28,00', '15,27', '43,273', '04069']`

Ordem dos itens nas listas extraídas:

0. Inscrição
1. Nome
2. Data nasicmento
3. Class
4. Nota final
5. CG
6. Nota (1 etapa)
7. disc1
8. disc2
9. disc3
10. CE
11. Red
12. Nota (2 etapa)
13. Opção 1

> Tamanho da lista: 14

### > *Ordem dos itens na *página 166**

Página 166 possui candidatos que escolheram 2 e 3 opções

Ex: 
`['6791805-0', 'GABRIEL CESAR', '17/06/99', '1', '06016 07016', '76,518', '79,762', '79,762', '11', '8', '10', '58,00', '15,27', '73,273', '05016']`

Ordem dos itens nas listas extraídas:

0. Inscrição
1. Nome
2. Data nasicmento
3. Class
4. **'Opção 2 Opção 3' -- ou somente opção Opção 2**
5. Nota final 
6. CG
7. Nota (1 etapa)
8. disc1
9. disc2
10. disc3
11. CE 
12. Redação
13. Notal final
14. Opção 1

> Tamanho da lista: 15

### > *Ordem dos itens na página 124*

Página 125 do PDF `data2.pdf` possui candidatos do curso de teatro que possuem a coluna *Hab* (habilidade) preenchida.

Ordem dos itens na lista extraída:

0. Inscrição
1. Nome
2. Data nascimento
3. Class
4. **Hab**
5. Nota final
6. CG
7. Nota (1 etapa)
8. disc1
9. disc2
10. disc3
11. CE
12. Redação
13. Nota (2 etapa)
14. Opção 1

> Tamanho da lista: 15

## Considerações

Após fazer explorar as diferentes saídas possíveis da extração de informação, nota-se alguns padrões:
- A ordem observada na página 1 é prioritária
- Quando uma nova coluna é preenchida, é inserida logo após *'Class'*
- A ordem que são inseridos (à direita de *'Class'*) segue a ordem do PDF (visualmente)
- O candidato nunca vai preencher Opção 1 e Opção 3. As possibilidades são:
    - Opção 1
    - Opção 1, Opção 2
    - Opção 1, Opção 2, Opção 3
- As opções se referem ao Grupo ao qual o candidato se inscreveu e o curso. Dessa forma:
    - **XXYYY:** Onde **XX** é o código do grupo e **YYY** o código do curso

### Ordem da lista retornada da função `extract_info`:

0. Inscrição
1. Nome
2. Data nascimento
3. Class
4. Opção 2
5. Opção 3
6. Habilidades
7. Nota final
8. CG
9. Nota (1 etapa)
10. disc1
11. disc2
12. disc3
13. CE
14. Redação
15. Nota (2 etapa)
16. Opção 1

> Tamanho final: 17

# PDF dos cursos

O PDF dos cursos contém informações referentes a quantas vagas são disponibilizadas para cada grupo de cada curso. No PDF dos candidatos, os nomes se repetem várias vezes, cada repetição se refere a um grupo o qual o candidato se inscreveu.

> **Obs:** Um curso possui vagas para diferentes grupos de candidatos, um candidato pode fazer parte de 1, 2 ou 3 desses grupos. 

Utilizando o pdf com a relação candidato/vaga, a lógica para a primeira chamada funciona da forma:

**Curso:** Sistemas de Informação\
**Grupos/vagas:** 
- 01006 (10 vagas)
- 02006 (8 vagas)
- 03006 (5 vagas)

**Candidato:** Fulano da Silva\
**Opções:** 02066, 03066

1. Se Fulano estiver entre os **8** primeiros na lista referente ao grupo 02006 (sua primeira opção), ele não é considerado na lista do grupo 03066 (sua segunda opção) e a vaga vai para o próximo da lista
2. Se Fulano não estiver entre os **8** primeiros da sua primeira opção (02006), mas estiver entre os **5** primeiros da sua segunda opção (03066), a vaga na sua segunda opção é dele. 

Dessa forma, extraímos a lista de cursos dos anos 2020, 2021 e 2022 na seguinte ordem:
1. Grupo (sem considerar o curso).
2. Quantas pessoas estão inscritas
3. Quantas vagas possui o grupo
4. Nome por extenso do curso
5. Ano do vestibular 
