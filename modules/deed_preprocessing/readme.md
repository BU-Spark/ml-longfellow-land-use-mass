# Deed Preprocessing Module

## preprocessor.py

Preprocessor accepts a string which should be the text output of an OCR model. It then calls spaCy NLP, and parses metadata from the returned object. The following loop handles the parsing:

```python
for sent in doc.sents:
        result["sentences"].append(sent.text)
        result["sentence_lengths"].append(len(sent))
        
        for token in sent:
            pos = token.pos_
            all_tokens.append(token.text)
            
            if pos in pos_groups:
                pos_groups[pos].append(token.text)
                
            result["dependencies"].append({
                "token": token.text,
                "dep": token.dep_,
                "head": token.head.text
            })
            result["token_offsets"].append({
                "token": token.text,
                "start": token.idx,
                "end": token.idx + len(token.text)
            })
```

See eda.ipynb for more analysis on these objects.

## read_tiffs.py

This module can be used to read TIFFs from a ZIP file and store result in a directory of text outputs called /outputs. Do the following steps:

- Make sure you set up Google Cloud OCR credentials first, see the README in../google_cloud_ocr to do this.
- Download a ZIP of TIFFs from the SCC or Google Cloud and rename it tiffs.zip. Put it in the deeds_preprocessing directory
- Run the script and see the output text files in /outputs, note that this will use Google Cloud credits
- Use preprocessor.py to structure the text files into spaCy objects

These steps are all done in eda.ipynb for further clarity.

## read_all_tiffs.py

This script is designed to be run in the SCC and submitted as a job with the accompanying file "ocr_deeds.sh". It loops through the specified folders within the SCC that contain deed TIF files and retrieves the OCR text of these deeds. Then it utilizes "bigotry-dict" which contains a set of national identifiers and checks if any word within the OCR text matches with any of these identifiers. If any of the words match, the file is put in ./racist and if not it is put in ./outputs. 
Before running:
-Make sure your Google Cloud OCR credentials are setup, see the README in../google_cloud_ocr to do this.
-Change the folders to be run on in line 

