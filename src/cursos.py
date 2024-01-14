from pypdf import PdfReader
import re

def extract_info(pdf_path, year: str):
    print(f'reading {pdf_path}')
    pdf = PdfReader(pdf_path)
    course_list = []
    for page in pdf.pages:
        text = page.extract_text()
        course_pattern = re.compile(r"[0-9]+,[0-9]+%\s*[A-z\u00C0-\u00ff\s'\.,-\/#!$%\^&\*;:{}=\-_`~()]+[0-9]+\s*[0-9]+\s*[0-9]+", re.MULTILINE)
        courses = course_pattern.findall(text)
        name_pattern = re.compile(r'([A-z\u00C0-\u00ff]+|\-)\s+', re.MULTILINE)
        for course in courses:
            name = name_pattern.findall(course)
            name = ' '.join(name)
            attributes = re.findall(r' [0-9]+', course)
            attributes.extend([name, year])
            course_list.append(attributes)
    return course_list
