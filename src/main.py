import io

import pytesseract
from fastapi import FastAPI, File, UploadFile
from PIL import Image

app = FastAPI()


@app.post("/extract-text/")
async def extract_text_from_image(file: UploadFile = File(...)):
    """
    Extract text from an uploaded image file using Tesseract OCR.

    :param file: Uploaded image file.
    :return: Extracted text or an error message.
    """
    try:
        contents = await file.read()
        image = Image.open(io.BytesIO(contents))
        text = pytesseract.image_to_string(image)
        return {"filename": file.filename, "text": text.strip()}
    except Exception as e:
        return {"error": f"Error processing the image: {e}"}
