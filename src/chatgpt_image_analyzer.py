import os
from typing import Dict, List

import pytesseract
from PIL import Image


class ChatGPTImageAnalyzer:
    def __init__(self, image_directory: str):
        """
        Initialize the ChatGPT Image Analyzer.

        :param image_directory: Path to the directory containing images to analyze.
        """
        self.image_directory = image_directory

    def get_image_files(self) -> List[str]:
        """
        Retrieve a list of image files in the specified directory.

        :return: List of image file paths.
        """
        supported_formats = [".jpg", ".jpeg", ".png", ".bmp", ".tiff"]
        return [
            os.path.join(self.image_directory, file)
            for file in os.listdir(self.image_directory)
            if os.path.splitext(file)[-1].lower() in supported_formats
        ]

    def extract_text_from_image(self, image_path: str) -> str:
        """
        Extract text from a single image using Tesseract OCR.

        :param image_path: Path to the image file.
        :return: Extracted text as a string.
        """
        try:
            image = Image.open(image_path)
            text = pytesseract.image_to_string(image)
            return text.strip()
        except Exception as e:
            return f"Error processing {image_path}: {e}"

    def analyze_images(self) -> Dict[str, str]:
        """
        Analyze all images in the directory and extract text from them.

        :return: Dictionary where keys are image file paths and values are extracted text.
        """
        image_files = self.get_image_files()
        analysis_results = {}

        for image_file in image_files:
            print(f"Analyzing image: {image_file}")
            text = self.extract_text_from_image(image_file)
            analysis_results[image_file] = text

        return analysis_results


if __name__ == "__main__":
    # Example usage
    directory_path = input("Enter the path to the image directory: ")
    analyzer = ChatGPTImageAnalyzer(directory_path)
    results = analyzer.analyze_images()

    output_path = os.path.join(directory_path, "analysis_results.txt")
    with open(output_path, "w") as output_file:
        for image, text in results.items():
            output_file.write(f"Image: {image}\nExtracted Text:\n{text}\n{'-'*80}\n")

    print(f"Analysis complete. Results saved to {output_path}")
