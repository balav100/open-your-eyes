import pdfplumber
import fitz

from modules.easyocr_handler import extract_text_easyocr


def extract_text_from_pdf(pdf_path):

    text = ""

    try:

        with pdfplumber.open(pdf_path) as pdf:

            for page in pdf.pages:

                extracted = page.extract_text()

                if extracted:
                    text += extracted + "\n"

        # OCR fallback
        if len(text.strip()) == 0:
            text = extract_text_easyocr(pdf_path)

        return text

    except Exception as e:
        return str(e)