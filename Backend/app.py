from flask import Flask, request, jsonify
import pdfplumber
from PIL import Image
import pytesseract
import mimetypes
from flask_cors import CORS
# import logging

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Configure logging
# logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

# Function to extract text from PDF
def extract_text_from_pdf(uploaded_file):
    try:
        with pdfplumber.open(uploaded_file) as pdf:
            text = ""
            for page in pdf.pages:
                text += page.extract_text()
            return ( text.strip() if text else "No text found in the PDF."),None
    except Exception as e:
        
        # logging.error(f"Error extracting text from PDF: {e}")
        return None, f"Error extracting text from PDF: {str(e)}"

# Function to extract text from Image
def extract_text_from_image(uploaded_file):
    try:
        image = Image.open(uploaded_file)
        text = pytesseract.image_to_string(image)
        return text.strip() if text else "No text found in the image."
    except Exception as e:
        # logging.error(f"Error extracting text from Image: {e}")
        return None, f"Error extracting text from Image: {str(e)}"

# Helper functions for file type validation
def is_pdf(file):
    return mimetypes.guess_type(file.filename)[0] == "application/pdf"

def is_image(file):
    mime_type = mimetypes.guess_type(file.filename)[0]
    return mime_type and mime_type.startswith("image")

# API endpoint for file uploads (PDF or image)
@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    
    file = request.files["file"]
    
    # Check if the file is a valid PDF or image and process accordingly
    if is_pdf(file):
        text, error = extract_text_from_pdf(file)
    elif is_image(file):
        text, error = extract_text_from_image(file)
    else:
        return jsonify({"error": "Uploaded file is not a valid PDF or image"}), 400

    if error:
        return jsonify({"error": error}), 500  # Return server error with error message
    
    return jsonify({"extracted_text": text}), 200

# Home route
@app.route("/")
def home():
    return jsonify({
        "message": "Flask server is running.",
        "instructions": {
            "upload": "/upload (POST with a file key named 'file')"
        }
    })

# Favicon route to avoid errors
@app.route('/favicon.ico')
def favicon():
    return "", 204  # Return an empty response with status 204 (No Content)

# Run the Flask app
if __name__== "__main__":
    app.run()