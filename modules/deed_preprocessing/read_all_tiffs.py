import os
import re
import zipfile
from spellcheck import correct_spelling
import importlib.util
from pathlib import Path
from difflib import SequenceMatcher

#to run this file, do "qsub ocr_tiffs.sh" in the scc terminal
#that command will run this file for up to 48 hours
#it will also create two files "ocr_tiffs.sh.e(job#)" and "ocr_tiffs.sh.o(job#)", which will show the errors and outputs of running this file, respectively
#you can delete both of these files after checking errors to clean up the repo

# Load the bigotry dictionary module
file_path = Path(__file__).resolve().parents[1] / "last_year" / "bigotry_dict.py"
spec = importlib.util.spec_from_file_location("bigotry_dict", str(file_path))
bigotry_dict_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bigotry_dict_module)
#load the google cloud ocr module
spec = importlib.util.spec_from_file_location("google_cloud_ocr", "../google_cloud_ocr/google_cloud_ocr.py")
google_cloud_ocr_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(google_cloud_ocr_module)

output_normal_dir = './outputs'
output_racist_dir = './racist'
bigotry_dict = bigotry_dict_module.bigotry_dict

os.makedirs(output_normal_dir, exist_ok=True)
os.makedirs(output_racist_dir, exist_ok=True)

#should always set these numbers to the most recent folders to be OCRed
#does not need to be a function because only running from the terminal and not in other files
for num in range(690,750):
    for root, dirs, files in os.walk(rf'../../../../mass-sec-state-deeds-data/Books 547-1849/{num}'):
        for file in files:
            
            if file.endswith('.TIF'):
                tiff_file_path = os.path.join(root, file)
                
                with open(tiff_file_path, 'rb') as tiff_file:
                    try:
                        extracted_text = google_cloud_ocr_module.google_cloud_ocr(tiff_file)
                        corrected_text = correct_spelling(extracted_text)
                        output_file_name = f"{os.path.splitext(file)[0]}.txt"

                        #search for words in the bigotry_dict, can update with additional words
                        found = False
                        words = re.split(r'[\n ]+', corrected_text)
                        for identifier in bigotry_dict.keys():
                            if not found:
                                for word in words:
                                    similarity_ratio = SequenceMatcher(None, word.lower(), identifier.lower()).ratio()
                                    if similarity_ratio >= 0.9:
                                        found = True
                                        break
                        
                        #put in respective folder
                        if found:
                            output_file_path = os.path.join(output_racist_dir, output_file_name)
                        else:
                            output_file_path = os.path.join(output_normal_dir, output_file_name)
                        
                        with open(output_file_path, 'w', encoding='utf-8') as output_txt:
                            output_txt.write(extracted_text)
                    
                    except Exception as e:
                        print(f"Error processing {file}: {str(e)}")

print("OCR processing complete. Text files are saved in:", output_normal_dir, "and in:", output_racist_dir)
