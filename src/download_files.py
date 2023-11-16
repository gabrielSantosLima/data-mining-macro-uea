from urllib.request import urlretrieve

from selenium import webdriver
from selenium.webdriver.common.by import By


def read_file(filename: str):
    file = open(filename)
    content  = file.read()
    file.close()
    return content

def split_links(content: str):
    return content.split('\n')

# 1. Acessar cada um dos links
# 2. Buscar pelo link do pdf cujo título tem as palavras (lista, candidatos, ordem, classificação)
# 3. Download de pdf
# 4. Salvar pdf localmente


def fetch_links(links: list[str]):
    pdfs: list[str] = []
    length_pdfs = len(links)

    driver = webdriver.Chrome(options=())

    for link in links:
        
        driver.get(link)
        driver.find_element(By.CSS_SELECTOR, "a[data-tabname='documento']").click()

        a = driver.find_elements('')

        urlretrieve()

        progress = len(pdfs)/length_pdfs * 100
        print(f'{progress:.0f}% concluído --- Link: {link}')

    driver.quit()
    return []

def download_files(filename: str):
    content = read_file(filename)
    links = split_links(content)
    pdf_paths = fetch_links(links)
    return pdf_paths

