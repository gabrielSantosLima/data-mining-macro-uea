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

# [x] Acessar cada um dos links
# [] Buscar pelo link do pdf cujo título tem as palavras (lista, candidatos, ordem, classificação)
# [] Download de pdf
# [] Salvar pdf localmente

def button_click(driver: webdriver.Chrome, classname: str):
    driver.execute_script(f"document.querySelector('.{classname}').click()")

def fetch_links(links: list[str]):
    pdfs: list[str] = []
    length_pdfs = len(links)

    driver = webdriver.Chrome()
    driver.maximize_window()

    for link in links:
        
        driver.get(link)

        document_button = None
        while document_button == None:
            document_button = driver.find_element(By.CLASS_NAME, "tab-link")

        button_click(driver, 'tab-link')

        tab_item = None
        while tab_item == None:
            tab_item = driver.find_element(By.CLASS_NAME, "course-tab-item") 

        link_elements = driver.execute_script('return document.querySelectorAll("a.pull-right");')
        pdf_links: list[str] = []

        for link_element in link_elements:
            pdf_links.append(link_element.href)

        progress = len(pdfs)/length_pdfs * 100
        print(f'{progress:.0f}% concluído --- Link: {link}')

    driver.quit()
    return []

def download_files(filename: str):
    content = read_file(filename)
    links = split_links(content)
    pdf_paths = fetch_links(links)
    return pdf_paths

