import os
import unittest

from src.chatgpt_image_analyzer import ChatGPTImageAnalyzer


class TestChatGPTImageAnalyzer(unittest.TestCase):
    def setUp(self):
        self.test_directory = "tests/test_images"
        os.makedirs(self.test_directory, exist_ok=True)
        self.analyzer = ChatGPTImageAnalyzer(self.test_directory)

    def tearDown(self):
        for file in os.listdir(self.test_directory):
            os.remove(os.path.join(self.test_directory, file))
        os.rmdir(self.test_directory)

    def test_get_image_files(self):
        with open(os.path.join(self.test_directory, "test.txt"), "w") as f:
            f.write("Not an image")
        self.assertEqual(len(self.analyzer.get_image_files()), 0)

    # Add more tests for text extraction and error handling


if __name__ == "__main__":
    unittest.main()
