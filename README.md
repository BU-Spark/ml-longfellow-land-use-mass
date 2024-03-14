![logo](logo.png)

# DRAINS: Deed Restriction Artificial Intelligence Notification System
SPARK! x MassMutual Data Days for Good

Created by Alessandra Lanz, Sahir Doshi, Cindy Zhang, Vijay Fisch, Sindhuja Kumar, Naman Nagaria, Valentina Haddad

## Project Overview
This project, developed for the [Longmeadow Historical Society](https://www.longmeadowhistoricalsociety.org), introduces an automated tool designed to identify racist restrictions within historical property deeds. Utilizing advanced text analysis techniques, the program processes TIFF images of property deeds, evaluates the text for racist content, and extracts critical information—specifically the deed date and page number—into a CSV format for efficient access and analysis.

### Key Features

- Image Processing: Accepts property deed images in TIFF format.
- Content Analysis: Employs text recognition and analysis algorithms to detect racist language.
- Data Extraction: Automates the extraction of deed date and page number for each document analyzed.

Our aim is to assist the Longmeadow Historical Society in their efforts to document and understand historical injustices, contributing to a broader societal recognition and rectification of past discriminations.

### Dataset Used
The historical property deeds (mainly 1900s) of Massachusetts.

## Quick Start
### Requirements
Install essential libraries:
```
pip install -r requirements.txt
```

### Set up OpenAI_API_KEY
In folder `modules`: 

1. Duplicate the file `env.template`

2. Add your `api key` and `organization id` to `OPENAI_API_KEY` and `OPENAI_ORG_ID`. You can get your api key and organization ID via the link: https://platform.openai.com/api-keys, 
https://platform.openai.com/account/organization

3. Rename this file to `.env`

> For different ChatGPT versions, you can change the `model` parameter in `racist_chatgpt_analysis.py`.   
It's on line 13:
`model="gpt-3.5-turbo"`  
To access ChatGPT-4, you can update this line to:
`model="gpt-4-0125-preview"`

### Run the code
In file `main.py`, change the folder path to your path(line 36).
```python
racism_threshold('/Your/Path/To/Files')
```
For the **Windows Operating System**, you need to edit the path manually to make sure all slashes are **backslashes**. 

Then in command line, run:
```
python main.py
```

## Modules Overview

`OCR.py`: Employs Google's OCR (Optical Character Recognition) technology, via the PyTesseract library, to convert deed images in TIFF format to searchable and analyzable text.

`bigotry_dict.py`: Contains a hardcoded dictionary of terms associated with racist language that is used to scrutinize the deed text for potential matches.

`locate.py`: Utilizes PyTesseract OCR to identify and extract specific information from the deed text, such as the deed date, book of origin, and page number.

`racist_chatgpt_analysis.py`: Integrates with OpenAI's ChatGPT API to process the text-based deeds for advanced racism detection, offering a nuanced analysis that goes beyond keyword matching.

`racist_text_query.py`: A failsafe text query module that acts as a backup for the ChatGPT analysis, manually checking deeds against the bigotry dictionary to ensure no instances of racist language are overlooked.