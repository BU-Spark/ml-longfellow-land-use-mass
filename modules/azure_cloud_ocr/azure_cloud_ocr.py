import os
import requests
from dotenv import load_dotenv

load_dotenv()

AZURE_OCR_URL = os.getenv('AZURE_OCR_URL')
AZURE_SUBSCRIPTION_KEY = os.getenv('AZURE_SUBSCRIPTION_KEY')

def azure_cloud_ocr(file):
    headers = {
        'Ocp-Apim-Subscription-Key': AZURE_SUBSCRIPTION_KEY,
        'Content-Type': 'application/octet-stream'
    }
    params = {
        'language': 'en',  
        'detectOrientation': 'true'
    }
    
    response = requests.post(AZURE_OCR_URL, headers=headers, params=params, data=file.read())
    
    if response.status_code != 200:
        raise Exception(f"Azure OCR error: {response.status_code}, {response.text}")
    
    result = response.json()

    lines = []
    for region in result.get('regions', []):
        for line in region.get('lines', []):
            line_text = " ".join([word['text'] for word in line['words']])
            lines.append(line_text)
    
    return "\n".join(lines)
