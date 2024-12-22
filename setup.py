from setuptools import find_packages, setup

setup(
    name="my_package",  # Replace with your package name
    version="0.1.0",
    description="A basic Python package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/my_package",  # Replace with your repo URL
    license="MIT",  # Use the license you want
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.6",
    install_requires=[
        # Add any package dependencies here, e.g., "numpy>=1.20.0"
        "pytesseract",
        "pillow",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
