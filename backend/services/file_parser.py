import PyPDF2
import docx

def extract_text_from_pdf(file_stream):
    """Extracts text from a PDF file stream."""
    try:
        pdf_reader = PyPDF2.PdfReader(file_stream)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        return text
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return "Error: Could not extract text from the PDF file."

def extract_text_from_docx(file_stream):
    """Extracts text from a DOCX file stream."""
    try:
        doc = docx.Document(file_stream)
        text = "\n".join([para.text for para in doc.paragraphs])
        return text
    except Exception as e:
        print(f"Error reading DOCX: {e}")
        return "Error: Could not extract text from the DOCX file."