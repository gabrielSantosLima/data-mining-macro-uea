import fitz
from fitz.fitz import Document
from os import listdir
from os.path import join
import re
import csv

def extract_info(pdf_path, year):
    pdf: Document = fitz.open(pdf_path)
    candidates = []
    print(f"reading {pdf_path}")
    for page in pdf:
        text = page.get_text()
        id_course, course_name = find_course(text)
        page_candidates = create_row_list(text, year, (id_course, course_name))
        candidates.extend(page_candidates)
    return candidates

"return: id_opcao, nome_curso"
def find_course(text: str) -> tuple:
    course_pattern = re.compile(r"^0[0-9]{4} - [A-z\u00C0-\u00ff\s'\.,-\/#!$%\^&\*;:{}=\-_`~()]* - [A-z\u00C0-\u00ff]+", re.MULTILINE)
    found_course = course_pattern.findall(text)
    course_info = found_course[0].split('-')
    
    return course_info[0], found_course[0][8:]

def split_options(lines: list) -> list[str]:
    content = lines[4]
    options = content.split(' ')
    if len(options) == 1:
        options.append('No')
    lines[4:4] = options
    lines.reverse()
    lines.remove(content)
    lines.reverse()
    if len(lines) == 16:
        lines.insert(6, 'No')
    return lines

def create_row_list(text: str, year:str, course: tuple) -> list[str]:
    id_pattern = re.compile(r'^[0-9]{7}-[0-9]{1}', re.MULTILINE)
    scape_pattern = r"([A-Z\s]+)\n([A-Z\s]+)"
    text = re.sub(scape_pattern, r'\1 \2', text)

    found_ids = id_pattern.findall(text)
    id_size = len(found_ids)
    
    page_candidates = []
    for i in range(id_size):
        begin_idx = text.find(found_ids[i])
        sub_str = ''
        if i + 1 < id_size:
            end_idx = text.find(found_ids[i+1])
            sub_str = text[begin_idx:end_idx]
        else:
            sub_str = text[begin_idx:]
            sub_str = sub_str.split('LstCls', 1)[0]
        lines = sub_str.split('\n')
        lines = [line.strip() for line in lines if line.strip()]
        size = len(lines)
        
        if re.match(r'[0-9]{5}', lines[4]):
            if size == 16 or size == 15:
                lines = split_options(lines)
            size = len(lines)
        else:
            if size == 15:
                lines[4:4] = ['No', 'No']
            elif size == 14:
                lines [4:4] = ['No', 'No', 'No']
        lines.extend([course[0], course[1], year])
        page_candidates.append(lines)
    return page_candidates

# years = [2019, 2019, 2019, 2020, 2021, 2022, 2022]
#     # # header = "numinscricao,nome,datanasc,classificao,NF,CG,ENEM,nota1,disc1,disc2,disc3,CE,RED,nota2,OP1,OP2,OP3\n"
# header = ["numinscricao","nome","datanasc","classificacao","opcao_curso_2","opcao_3_curso",
#               "habilidades","nota_final","nota_cg","nota_etapa_1","disc1","disc2","disc3",
#               "nota_ce","nota_redacao","nota_etapa_2","opcao_curso_1", "id_curso_escolhido", "nome_curso_escolhido", "ano"]
# dataset(r'C:\Users\SAMSUNG\Documents\GitHub\data-mining-macro-uea\data\pdf\candidatos', 'data.csv', header, years)
# pdf: Document = fitz.open(r'C:\Users\SAMSUNG\Documents\GitHub\data-mining-macro-uea\data\pdf\candidatos\2019\data1.pdf')