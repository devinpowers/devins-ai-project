import io

from fastapi.testclient import TestClient
from PIL import Image

from src.main import app

client = TestClient(app)


# Utility to create an in-memory image for testing
def create_test_image(format="JPEG"):
    image = Image.new("RGB", (100, 100), color=(255, 255, 255))
    buffer = io.BytesIO()
    image.save(buffer, format=format)
    buffer.seek(0)
    return buffer


def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert "Welcome to the Image Text Extractor API" in response.json()["message"]


def test_extract_text_info_endpoint():
    response = client.get("/extract-text/")
    assert response.status_code == 200
    assert "This endpoint accepts POST requests" in response.json()["message"]


def test_status_endpoint():
    response = client.get("/status/")
    assert response.status_code == 200
    assert response.json() == {
        "status": "API is operational",
        "message": "Everything is running smoothly!",
    }


def test_supported_formats_endpoint():
    response = client.get("/supported-formats/")
    assert response.status_code == 200
    assert "Supported image formats" in response.json()["message"]
    assert "JPEG" in response.json()["formats"]


def test_extract_text_from_image():
    test_image = create_test_image()
    files = {"file": ("test.jpg", test_image, "image/jpeg")}

    response = client.post("/extract-text/", files=files)
    assert response.status_code == 200
    assert response.json()["filename"] == "test.jpg"
    assert "text" in response.json()  # Text content from the image


def test_extract_text_from_image_invalid_file():
    files = {"file": ("test.txt", io.BytesIO(b"invalid data"), "text/plain")}

    response = client.post("/extract-text/", files=files)
    assert response.status_code == 200
    assert "error" in response.json()
    assert "Error processing the image" in response.json()["error"]


def test_extract_metadata_endpoint():
    test_image = create_test_image("JPEG")
    files = {"file": ("test.jpg", test_image, "image/jpeg")}

    response = client.post("/extract-metadata/", files=files)
    assert response.status_code == 200
    metadata = response.json()

    assert metadata["filename"] == "test.jpg"
    assert metadata["format"] == "JPEG"
    assert metadata["size"] == [100, 100]  # Expected dimensions
    assert metadata["mode"] == "RGB"


def test_extract_metadata_invalid_file():
    files = {"file": ("test.txt", io.BytesIO(b"invalid data"), "text/plain")}

    response = client.post("/extract-metadata/", files=files)
    assert response.status_code == 200
    assert "error" in response.json()
    assert "Error extracting metadata" in response.json()["error"]
