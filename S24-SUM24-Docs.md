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

`pagenum.py`: A failsafe page number extraction module that acts as a backup for the data extraction done by `locate.py` by cropping the corners of the image for enlargement and easy OCR translation. 


# PIT-NE x SPARK! x MassMutual ~ SUMMER 2024 

Created by Arnav Sodhani, Grace Chong, Hannah Choe

## Project Overview

This project is developed for the Longmeadow Historical Society and is a direct continuation of the work done by SPARK! x MassMutual Data Days for Good. 

This interactive map shows the temporal progression of racist deeds in a neighborhood in Longmeadow, MA in the early 1900s. To make this product, we first utilized the MA registry and filtered off of Hampden County to get our data. On the registry website, we filtered out property deeds based on whether the seller was E.H. Robbins (this builder was infamous for placing racial restrictions in deeds) and the period was the early 1900s (MA passed the Fair Housing Act in 1946 so we had to look for deeds prior that year). We then organized and consolidated these deeds in a spreadsheet. Next, we filtered whether the deed had any racial restrictions and then normalized the spreadsheet so that each "lot number" had its row. Lastly, to finalize the creation of this database, we added two new columns: Address Today (we matched each "lot number" to its respective current-day address using GIS technology and the Longmeadow lot plan) and House Image (we matched each address to its house image using Google Maps). And then finally we used ArcGIS, software that helps to build web maps, to create our end deliverable of an interactive map that visualizes the data with a temporal aspect (time slider).

### Key Features 

-Cover and information page 

-Time slider of the existence of deeds 

-House icon: information on property deed 

-Address search tool

-Filter tool for racial groups 

### Process

Data Collection - 

There were issues running the code from SPARK! x MassMutual Data Days for Good. We decided to manually collect data from the Hampden County Registry of Deeds in Longmeadow, MA with E.H Robbins as the grantor. 

Data Cleaning and Transformation -
1. After manually collecting the data of racist deeds in Longmeadow with E.H Robbins as the grantor, we normalized the Lot # column to ensure that each Lot # has a unique row; this is so, because deeds may have multiple lot #s. 
2. Then we matched the lot # to the modern-day addresses using an existing Longmeadow GIS. 
3. Finally, we created a reference table with ID keys to map onto our GIS. 


### Visualization 

We chose ArcGIS for our visualization software (interactive map). 

Link to the ArcGIS instant app:
https://arcg.is/1aKD9b1
