from pypdf import PdfReader
import re

# chamadas = r'C:\Users\SAMSUNG\Documents\GitHub\data-mining-macro-uea\data\pdf\chamadas\2019\2019.pdf'

# pdf = PdfReader(chamadas)
# page = pdf.pages[0]
# text = page.extract_text()

# partes = text.split('\n')[2:]
# # print(partes)

# names = []

# for name in partes:
#     if not name.isdigit():
#        names.append(name.split('-')[0])

# names = [string.rstrip() for string in names]
# print(names)

def extract_info(pdf_path: str, year: str):
    print(f'reading {pdf_path}')
    pdf = PdfReader(pdf_path)
    names = []
    for page in pdf.pages:
        text = page.extract_text()
        lines = text.split('\n')[2:]
        for candidate in lines:
            if not candidate.isdigit():
                name = candidate.split('-')[0].rstrip()
                rgx = r'\b\d+(?:[.\'-]*\d+)*(?:[.\'-]*\d+)?[A-Za-z]*\b.*?\b(\d+)\b'
                match = re.search(rgx, candidate)
                if match:
                    names.append([name, match.group(1), year])
                else:
                    names.append([name, '', year])
    return names




