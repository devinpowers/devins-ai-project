import os

from setuptools import find_packages, setup


def parse_requirements(filename):
    """Parse dependencies from a requirements file."""
    with open(filename, "r") as f:
        return [line.strip() for line in f if line.strip() and not line.startswith("#")]


setup(
    name="my_package",
    version="0.1.0",
    description="A basic Python package for extracting text from images",
    long_description=open("README.md").read() if os.path.exists("README.md") else "",
    long_description_content_type="text/markdown",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/my_package",
    license="MIT",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.6",
    install_requires=parse_requirements("requirements.txt"),  # Parse requirements.txt
    extras_require={
        "dev": ["pytest", "flake8", "black"],  # Add optional development dependencies
    },
    entry_points={
        "console_scripts": [
            "extract-text=my_package.main:app",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords="OCR Tesseract image text extraction",
    test_suite="tests",
)
