import PyPDF2
from fpdf import FPDF
import re

def extract_pdf_text(uploaded_file):
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

def clean_notes(raw_text):
    # Remove extra whitespace and newlines
    cleaned = re.sub(r'\n+', '\n', raw_text)
    cleaned = re.sub(r' +', ' ', cleaned)
    # Remove bullet points if they are checkboxes
    cleaned = re.sub(r'☐', '', cleaned)
    return cleaned.strip()

def export_clean_pdf(cleaned_text):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    # Encode to latin-1, ignoring characters that can't be encoded
    safe_text = cleaned_text.encode('latin-1', 'ignore').decode('latin-1')
    pdf.multi_cell(0, 10, safe_text)
    output_path = "clean_notes.pdf"
    pdf.output(output_path)
    return output_path
