import os
import io
from dotenv import load_dotenv
from google.cloud import vision

load_dotenv()

google_creds = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')

if google_creds is None:
    raise EnvironmentError("GOOGLE_APPLICATION_CREDENTIALS not set in .env file")

client = vision.ImageAnnotatorClient()

def google_cloud_ocr(tiff_file):
    content = tiff_file.read()
    image = vision.Image(content=content)
    response = client.document_text_detection(image=image)
    text = response.full_text_annotation.text
    if response.error.message:
        raise Exception(f'API Error: {response.error.message}')

    return text
