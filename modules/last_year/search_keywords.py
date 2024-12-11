import os
import re
from difflib import SequenceMatcher
from bigotry_dict import bigotry_dict
#can also submit this with "qsub manual_keyword_check.sh" because it takes a long time

# Path to save the output
output_file_path = "output.txt"

# Open the output file in append mode
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    # Walk through the directory
    for root, dirs, files in os.walk(r'../deed_preprocessing/racist'):
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
                                            # Collect the surrounding words
                                            context = words[max(0, i-10):min(len(words),i+10)]
                                            context_str = ' '.join(context)

                                            # Write to the output file
                                            output_file.write(f"Context: {context_str}\n")
                                            output_file.write(f"File: {txt_file_path}\n\n")
                                            print(txt_file_path)
                                            found = True
                                    else:
                                        break
                            else:
                                break
                                    

                    except Exception as e:
                        print(f"Error processing {file}: {str(e)}")

print(f"Results saved to {output_file_path}")
