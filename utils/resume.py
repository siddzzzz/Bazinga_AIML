
from PyPDF2 import PdfReader
def to_string(loc):
    reader = PdfReader(loc)
    resume = ""
    for page in reader.pages:
        resume += page.extract_text()
    return resume