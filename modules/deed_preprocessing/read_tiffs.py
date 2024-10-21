import os
import zipfile
import importlib.util
from spellcheck import correct_spelling

spec = importlib.util.spec_from_file_location("google_cloud_ocr", "../google_cloud_ocr/google_cloud_ocr.py")
google_cloud_ocr_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(google_cloud_ocr_module)

zip_path = 'tiffs.zip'
output_dir = './outputs'

os.makedirs(output_dir, exist_ok=True)

with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall('./tiffs')

for root, dirs, files in os.walk('./tiffs'):
    for file in files:
        if file.endswith('.TIF'):
            tiff_file_path = os.path.join(root, file)
            
            with open(tiff_file_path, 'rb') as tiff_file:
                try:
                    print(tiff_file_path)
                    extracted_text = google_cloud_ocr_module.google_cloud_ocr(tiff_file)

                    # spell check the extracted text
                    corrected_text = correct_spelling(extracted_text)
                    
                    output_file_name = f"{os.path.splitext(file)[0]}.txt"
                    output_file_path = os.path.join(output_dir, output_file_name)
                    
                    with open(output_file_path, 'w', encoding='utf-8') as output_txt:
                        output_txt.write(extracted_text)
                
                except Exception as e:
                    print(f"Error processing {file}: {str(e)}")

print("OCR processing complete. Text files are saved in:", output_dir)
