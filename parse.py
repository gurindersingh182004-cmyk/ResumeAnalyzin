from PyPDF2 import PdfReader
import io



def parse_pdf(file):
    pdf_stream = io.BytesIO(file)