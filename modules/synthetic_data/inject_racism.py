import os
import random
import spacy

nlp = spacy.load("en_core_web_sm")

input_directory = "../../../../projectnb/sparkgrp/njquisel/ml-longfellow-land-use-mass/modules/deed_preprocessing/outputs"
output_directory = "./synthetic_data"
os.makedirs(output_directory, exist_ok=True) 

def create_synthetic_deeds(strings):
    text_files = [f for f in os.listdir(input_directory) if f.endswith('.txt')]
    
    for i, string in enumerate(strings):
        selected_file = random.choice(text_files)
        input_path = os.path.join(input_directory, selected_file)
        
        with open(input_path, 'r') as file:
            content = file.read()
        
        doc = nlp(content)
        sentences = [sent.text for sent in doc.sents]
        
        middle_index = len(sentences) // 2
        sentences.insert(middle_index, string)
        
        modified_content = ' '.join(sentences)
        output_path = os.path.join(output_directory, f"RACIST_{i}_{selected_file}")
        with open(output_path, 'w') as file:
            file.write(modified_content)
        
        print(f"Saved modified file: {output_path}")

strings_to_insert = ["Example insertion string 1", "Example insertion string 2", "Example insertion string 3"]
create_synthetic_deeds(strings_to_insert)
