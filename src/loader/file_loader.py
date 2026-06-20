import pdfplumber
import docx

def load_pdf(file_path):
    text=""
    with pdfplumber.open(file_path)as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text

def load_docx(file_path):
    doc = docx.Document(file_path)
    return"\n".join([para.text for para in doc.paragraphs])

def load_resume_file(file_path):
    if file_path.endswith(".txt"):
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    elif file_path.endswith(".pdf"):
        return load_pdf(file_path)
    elif file_path.endswith(".docx"):
        return load_docx(file_path)
    return ""
    