from os.path import join
from os import listdir
import csv

def get_pdf_paths(pdf_folder_path: str) -> list[str]:
    pdf_folder = listdir(pdf_folder_path)
    pdfs: list[str] = []
    years: list[int] = []

    for folder in pdf_folder:
        pdfs_by_year_path = join(pdf_folder_path, folder) # default_path + "year"
        pdfs_by_year = listdir(pdfs_by_year_path)
        years.append(folder)
        for pdf in pdfs_by_year:
            pdf_path = join(pdfs_by_year_path, pdf) # default_path + "year" + "pdf filename"
            pdfs.append(pdf_path) # save file paths
    
    return pdfs

def dataset(pdf_path: str, filename: str, header: str, years: list[str], extract_option) -> str:
    csv_path = join('.', 'data', 'csv')
    out_path = join(csv_path, filename)

    if filename in listdir(csv_path):
        print(f'{filename} already exists.')
        return out_path
    
    pdfs = get_pdf_paths(pdf_path)
    csv_file = open(out_path, 'w', newline='', encoding='utf-8')
    writer = csv.writer(csv_file)
    writer.writerow(header)

    for pdf, year in zip(pdfs, years):
        pdf_content = extract_option(pdf, year)
        writer.writerows(pdf_content)
    
    csv_file.close()
    return out_path

# from os import listdir
# from os.path import join
# from re import findall, sub

# from pypdf import PdfReader

# # [X] Ler todos os PDFs
# # [X] Extrair as tabelas de notas
# # [X] Criar um CSV com todas as notas

# def get_pdf_content(pdf_path: str) -> list[str]:
#     print(f"reading {pdf_path}")
#     reader = PdfReader(pdf_path)
    
#     candidates = []
#     for page in reader.pages:
#         text = page.extract_text()
#         # find all table rows by a regex expression 
#         full_texts = findall("(?=([0-9]{7}-[0-9]{1} [ \w]+ [0-9]{2}\/[0-9]{2}\/[0-9]{2}( +[0-9]+(,[0-9]+)?)+))", text)

#         for full_text in full_texts:
#             candidate: str = full_text[0]
#             candidate = candidate.strip().replace(',', '.').replace('  ', ',')
#             candidate = sub("\s(?=[0-9])", ',', candidate)
#             candidate = candidate.replace(' ', ',', 1)
#             candidates.append(f"{candidate}\n")

#     return candidates

# def get_pdf_paths(pdf_folder_path: str) -> list[str]:
#     pdf_folder = listdir(pdf_folder_path)
#     pdfs: list[str] = []
    
#     for pdf_folder in pdf_folder:
#         pdfs_by_year_path = join(pdf_folder_path, pdf_folder) # default_path + "year"
#         pdfs_by_year = listdir(pdfs_by_year_path)
#         for pdf in pdfs_by_year:
#             pdf_path = join(pdfs_by_year_path, pdf) # default_path + "year" + "pdf filename"
#             pdfs.append(pdf_path) # save file paths
    
#     return pdfs

# def dataset(pdf_folder_path: str, csv_name: str) -> str:
#     csv_path = join('.', 'data', 'csv')
#     filename = 'data.csv'
#     out_path = join(csv_path, filename)

#     if filename in listdir(csv_path):
#         print(f'{csv_name} already exists.')
#         return out_path

#     pdfs = get_pdf_paths(pdf_folder_path)
#     csv_file = open(out_path, 'a+')

#     header = "numinscricao,nome,datanasc,classificao,NF,CG,ENEM,nota1,disc1,disc2,disc3,CE,RED,nota2,OP1,OP2,OP3\n"
#     csv_file.write(header)
    
#     for pdf in pdfs:
#         pdf_content = get_pdf_content(pdf)
#         print(pdf_content)
#         csv_file.write(" ".join(pdf_content))

#     csv_file.close()

#     return out_path

# dataset(r'C:\Users\SAMSUNG\Documents\GitHub\data-mining-macro-uea\data\pdf', 'data.csv')
