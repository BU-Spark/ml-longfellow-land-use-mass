import os
import io
from dotenv import load_dotenv
from google.cloud import vision
from google.cloud import language_v1

load_dotenv()

google_creds = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')

if google_creds is None:
    raise EnvironmentError("GOOGLE_APPLICATION_CREDENTIALS not set in .env file")

client = vision.ImageAnnotatorClient()

def detect_text_tiff(path):
    """Detects text in a TIFF document."""
    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.document_text_detection(image=image)

    text = response.full_text_annotation.text

    if response.error.message:
        raise Exception(f'API Error: {response.error.message}')

    return text

def save_text_to_file(text, output_file):
    """Saves the extracted text to a file."""
    with open(output_file, 'w') as f:
        f.write(text)

if __name__ == "__main__":
    written_tiff_path = "./written.tiff"
    typed_tiff_path = "./typed.tiff"

    print("Processing written deed...")
    written_text = detect_text_tiff(written_tiff_path)
    
    save_text_to_file(written_text, 'written_deed_output.txt')

    print("\nProcessing typed deed...")
    typed_text = detect_text_tiff(typed_tiff_path)
    
    save_text_to_file(typed_text, 'typed_deed_output.txt')
