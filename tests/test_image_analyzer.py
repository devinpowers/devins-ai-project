import os

from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)

# Get the directory of the current test file
TESTS_DIR = os.path.dirname(__file__)


def test_extract_text_from_image_valid():
    """
    Test the `/extract-text/` endpoint with a valid image.
    """
    # Construct the full path to the sample image
    image_path = os.path.join(TESTS_DIR, "sample_image.png")
    with open(image_path, "rb") as image_file:
        response = client.post(
            "/extract-text/",
            files={"file": ("sample_image.png", image_file, "image/png")},
        )

    assert response.status_code == 200
    response_data = response.json()
    assert "filename" in response_data
    assert response_data["filename"] == "sample_image.png"
    assert "text" in response_data
    assert len(response_data["text"]) > 0  # Ensure some text was extracted


def test_extract_text_from_image_invalid():
    """
    Test the `/extract-text/` endpoint with an invalid file type.
    """
    # Construct the full path to the sample text file
    text_path = os.path.join(TESTS_DIR, "sample_text.txt")
    with open(text_path, "rb") as text_file:
        response = client.post(
            "/extract-text/",
            files={"file": ("sample_text.txt", text_file, "text/plain")},
        )

    assert response.status_code == 200
    response_data = response.json()
    assert "error" in response_data
    assert "Error processing the image" in response_data["error"]
