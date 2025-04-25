
import google.generativeai as genai
import fitz  # PyMuPDF to read PDF files
import os

from dotenv import load_dotenv
from pathlib import Path
load_dotenv(Path(".env"))

def load_knowledge_base(pdf_path="/data.pdf"):
    """
    Load the knowledge base from a PDF file and return its text content.
    
    Args:
    - pdf_path (str): The path to the PDF file.
    
    Returns:
    - text (str): The combined text from all pages in the PDF.
    """
    doc = fitz.open(pdf_path)
    text = ""
    
    # Extract text from each page in the PDF
    for page in doc:
        text += page.get_text()
    
    return text


# Configure with your API key
genai.configure(api_key=os.getenv('API_KEY'))

def ask_gemini(prompt, context):
    # Use gemini-1.5-flash for content generation
    model = genai.GenerativeModel("models/gemini-1.5-flash")  # Use Gemini 1.5 Flash
    response = model.generate_content(f"{context}\n\nUser: {prompt}")
    return response.text

