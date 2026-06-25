# Business Card Scanner

## Project Description
This project is an AI-powered Business Card Scanner built with Python. It utilizes OpenCV for image preprocessing (grayscale conversion and thresholding) and the Tesseract OCR engine to extract raw text from uploaded business card images. Regular Expressions are then applied to automatically parse contact information such as emails and phone numbers. The interactive interface is built using Streamlit.


## How to Run Locally
To run this project on your machine, follow these steps:
1. Clone this repository.
2. Ensure Tesseract-OCR is installed on your local system.
3. Install the required Python packages: `pip install -r requirements.txt`
4. Start the Streamlit application: `python -m streamlit run app.py`

## Used Dataset
No external dataset was required for model training, as this project utilizes the pre-trained Tesseract OCR engine. Sample business card images with clear contrast were sourced from public image repositories strictly for testing the pipeline in the Jupyter Notebook.

## Team Contribution
(Joliana Safwat): Developed the complete pipeline, including the Jupyter Notebook experiments, the OpenCV image processing logic, the regex text extraction, and the Streamlit user interface.