from PyPDF2 import PdfReader
import io

##This function takes in a pdf and reads it to give out the text
def parse_pdf(file):
    pdf_stream = io.BytesIO(file)
    

    # 2. Extract text
    reader = PdfReader(pdf_stream)

    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""

    text = text[:3000]## limiting the chars here 
    return text