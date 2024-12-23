# Use Python 3.9 slim base image
FROM python:3.9-slim

# Install Tesseract OCR and related dependencies
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    libtesseract-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements.txt and install Python dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy application files to the container
COPY . /app
WORKDIR /app

# Expose the port for the application
EXPOSE 8000

# Command to start the FastAPI application using uvicorn
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
