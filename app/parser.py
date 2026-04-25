import os
import fitz
from docx import Document
from app.utils import clean_text


def extract_text_from_pdf(file_path: str) -> str:
    text = ""

    pdf = fitz.open(file_path)

    for page in pdf:
        text += page.get_text()

    pdf.close()
    return clean_text(text)


def extract_text_from_docx(file_path: str) -> str:
    doc = Document(file_path)
    text = ""

    for paragraph in doc.paragraphs:
        text += paragraph.text + "\n"

    return clean_text(text)


def extract_resume_text(file_path: str) -> str:
    extension = os.path.splitext(file_path)[1].lower()

    if extension == ".pdf":
        return extract_text_from_pdf(file_path)

    if extension == ".docx":
        return extract_text_from_docx(file_path)

    raise ValueError("Only PDF and DOCX files are supported.")
