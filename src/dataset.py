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