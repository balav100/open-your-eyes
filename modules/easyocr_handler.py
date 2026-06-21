import easyocr
import fitz
import cv2
import numpy as np

reader = easyocr.Reader(['en'])


def extract_text_easyocr(pdf_path):

    doc = fitz.open(pdf_path)

    text = ""

    for page_num in range(len(doc)):

        page = doc.load_page(page_num)

        pix = page.get_pixmap()

        img = np.frombuffer(
            pix.samples,
            dtype=np.uint8
        ).reshape(
            pix.height,
            pix.width,
            pix.n
        )

        results = reader.readtext(img)

        for result in results:
            text += result[1] + " "

    return text