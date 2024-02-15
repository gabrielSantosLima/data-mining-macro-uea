from src.dataset import dataset
from src.candidatos import extract_info as candidate_info
from src.cursos import extract_info as course_info
from src.chamadas import extract_info as chamadas_info

candidate_path = r'C:\Users\SAMSUNG\Documents\GitHub\data-mining-macro-uea\data\2023'
years = [2023, 2023]
header = ["numinscricao","nome","datanasc","classificacao","opcao_curso_2","opcao_3_curso",
              "habilidades","nota_final","nota_cg","nota_etapa_1","disc1","disc2","disc3",
              "nota_ce","nota_redacao","nota_etapa_2","opcao_curso_1", "id_referencia_curso", "nome_referencia_curso", "ano"]
dataset(candidate_path, '2023_candidates_info.csv', header, years, candidate_info)
# print()
# course_path = r'C:\Users\SAMSUNG\Documents\GitHub\data-mining-macro-uea\data\pdf\cursos'
# header = ['grupo', 'qtde_inscritos', 'qtde_vagas', 'nome_curso', 'ano']
# years = [2020, 2021, 2022]
# dataset(course_path, 'course_info.csv', header=header, years=years, extract_option=course_info)

# chamadas_path = r'C:\Users\SAMSUNG\Documents\GitHub\data-mining-macro-uea\data\pdf\chamadas'
# years = [2019, 2020, 2021, 2022]
# header = ['nome', 'id_curso_aprovado', 'ano']
# dataset(chamadas_path, 'approved_candidates.csv', header, years, chamadas_info)
