Social Media Content Analyzer - Backend
Description
This repository contains the Flask-based backend for the Social Media Content Analyzer. It processes uploaded files, extracts text using OCR and PDF parsing, and provides engagement suggestions for social media posts.

Features
File upload support for PDFs and images.
Text extraction using OCR.
Engagement suggestion generation.
JSON-based API responses for seamless frontend interaction.
Error handling and logging.
Tech Stack
Backend Framework: Flask
OCR Library: Tesseract
PDF Parsing: PyPDF2
Deployment: Hosted on a server or cloud platform.
Setup Instructions
1. Clone the Repository
bash git clone https://github.com/codingproX/Backend.git cd Backend

2. Set up a Virtual Environment
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install Dependencies
   pip install -r requirements.txt
4. Set Environment Variables
  Create a .env file in the root directory.
Add the following:
FLASK_ENV=development
FLASK_APP=app.py
5. Run the Flask Server
   flask run
   The backend will run on http://localhost:5000.
API Documentation
Base URL http://localhost:5000

Endpoints
 POST /upload
 Description: Upload a PDF or image file for text extraction and analysis.
 Request:
 Headers: Content-Type: multipart/form-data
 Body: File upload (file key).
Response:
Success (200):{
"status": "success",
"suggestions": [
"Add hashtags",
"Include a call-to-action",
"Use more concise sentences"
]
}

Error (400):

 {
  "status": "error",
   "message": "Invalid file format"
  }
Deployment
To deploy the backend, use a cloud platform like AWS, Heroku, or Render. Use Gunicorn for a production-ready server:

gunicorn app:app
3. Add README.md to Repositories
1. Navigate to Your Repository Folder:
bash cd

2. Create or Replace the README.md File:
Copy the above respective content into a README.md file in each repository.
3. Commit and Push the Changes:
git add README.md
git commit -m "Added project documentation"
git push origin main
Deployment
Frontend Deployment
Build the frontend:
npm run build
Deploy the build folder to Netlify.
Ensure the backend URL is correctly set in the .env file.
Backend Deployment
Use a cloud platform such as AWS, Heroku, or Render.
Ensure all dependencies are installed and environment variables are set.
Run the Flask app with a production-ready server like Gunicorn:
About
backend-three-fawn-84.vercel.app
Resources
 Readme
 Activity
Stars
 0 stars
Watchers
 1 watching
Forks
 0 forks
Report repository
Releases
No releases published
Packages
No packages published
Deployments
6
 Production 8 months ago
+ 5 deployments
Languages
Python
98.2%
 
Procfile
1.8%
Footer
