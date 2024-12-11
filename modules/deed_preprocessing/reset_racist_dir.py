import os
import shutil
import re
from difflib import SequenceMatcher
import importlib.util
from pathlib import Path

#This process should take a long time, so I would do "qsub reset_racist_dir.sh" to submit as an SCC job

file_path = Path(__file__).resolve().parents[1] / "last_year" / "bigotry_dict.py"
spec = importlib.util.spec_from_file_location("bigotry_dict", str(file_path))
bigotry_dict_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bigotry_dict_module)

bigotry_dict = bigotry_dict_module.bigotry_dict

source_dir = "./racist"
destination_dir = "./outputs"

if not os.path.exists(source_dir) or not os.path.exists(destination_dir):
    #if this prints, restart
    print(f"Source directory '{source_dir}' or destination directory '{destination_dir}' does not exist.")
else:
    #moves all files in the ./racist directory into the ./outputs directory
    #should leave ./racist directory empty and ready to repopulate
    for file_name in os.listdir(source_dir):
        if file_name.endswith('.txt'):
            source_file = os.path.join(source_dir, file_name)
            destination_file = os.path.join(destination_dir, file_name)

            # Skip if not a file
            if not os.path.isfile(source_file):
                continue

            # Check for duplicates and only move if not a duplicate
            if not os.path.exists(destination_file):
                #CHECK TO MAKE SURE THIS PART WORKS, worried destination_file is wrong
                shutil.move(source_file, destination_file)
                print(f"Moved: {file_name} -> {destination_dir}")

    #go through every deed in ./outputs and check if that deed contains a word in 'bigotry_dict'
    for root, dirs, files in os.walk(r'../deed_preprocessing/outputs'):
        for file in files:
            if file.endswith('.txt'):
                txt_file_path = os.path.join(root, file)

                with open(txt_file_path, 'rb') as txt_file:
                    try:
                        # Read and decode the text file
                        text = txt_file.read()
                        decoded_text = text.decode('utf-8')
                        words = re.split(r'[\n ]+', decoded_text)

                        # Look for matches in the text
                        found = False
                        for i in range(len(words)):
                            if not found:
                                for identifier in bigotry_dict.keys():
                                    if not found:
                                        similarity_ratio = SequenceMatcher(None, words[i].lower(), identifier.lower()).ratio()
                                        if similarity_ratio >= 0.9:
                                            #figure out how to move this file into other directory
                                            found = True
                                    

                    except Exception as e:
                        print(f"Error processing {file}: {str(e)}")
    


