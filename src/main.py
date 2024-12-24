import io

import pytesseract
from fastapi import FastAPI, File, UploadFile
from PIL import ExifTags, Image

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


@app.get("/")
def root():
    """
    Root endpoint providing basic usage instructions.
    """
    return {
        "message": "Welcome to the Image Text Extractor API! Use /extract-text/ to upload an image."
    }


@app.get("/extract-text/")
def extract_text_info():
    """
    Provide usage details for the text extraction endpoint.
    """
    return {
        "message": "This endpoint accepts POST requests with an image file to extract text."
    }


@app.get("/status/")
def check_status():
    """
    Check the operational status of the API.
    """
    return {
        "status": "API is operational",
        "message": "Everything is running smoothly!",
    }


@app.get("/supported-formats/")
def supported_formats():
    """
    List supported image formats for text extraction.
    """
    formats = ["JPEG", "PNG", "TIFF", "BMP", "GIF"]
    return {
        "message": "Supported image formats for text extraction.",
        "formats": formats,
    }


@app.post("/extract-metadata/")
async def extract_metadata(file: UploadFile = File(...)):
    """
    Extract metadata from an uploaded image file.

    :param file: Uploaded image file.
    :return: Image metadata (e.g., dimensions, format).
    """
    try:
        contents = await file.read()
        image = Image.open(io.BytesIO(contents))

        # Extract basic metadata
        metadata = {
            "filename": file.filename,
            "format": image.format,
            "size": image.size,  # (width, height)
            "mode": image.mode,  # Color mode (e.g., RGB, CMYK)
        }

        # Extract EXIF data if available
        exif_data = image._getexif()
        if exif_data:
            metadata["exif"] = {
                ExifTags.TAGS.get(tag, tag): value
                for tag, value in exif_data.items()
                if tag in ExifTags.TAGS
            }

        return metadata
    except Exception as e:
        return {"error": f"Error extracting metadata: {e}"}
