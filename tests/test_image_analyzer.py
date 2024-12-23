from fastapi.testclient import TestClient

from src import main

client = TestClient(main.app)


def test_extract_text_from_image_valid():
    """
    Test the `/extract-text/` endpoint with a valid image.
    """
    # Use a small sample image for testing
    with open("sample_image.png", "rb") as image_file:
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
    # Send a non-image file
    with open("sample_text.txt", "rb") as text_file:
        response = client.post(
            "/extract-text/",
            files={"file": ("sample_text.txt", text_file, "text/plain")},
        )

    assert response.status_code == 200
    response_data = response.json()
    assert "error" in response_data
    assert "Error processing the image" in response_data["error"]
