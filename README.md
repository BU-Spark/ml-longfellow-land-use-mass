# TEMPLATE-base-repo

All Pull Requests must follow the Pull Request Template, with a title formatted like such `[Project Name]: <Descriptive Title>`
![logo](logo.png)

# DRAINS: Deed Restriction Artificial Intelligence Notification System

## Project Overview
This project, developed for the [Longmeadow Historical Society](https://www.longmeadowhistoricalsociety.org), introduces an automated tool designed to identify racist restrictions within historical property deeds. Utilizing advanced text analysis techniques, the program processes TIFF images of property deeds, evaluates the text for racist content, and extracts critical information—specifically the deed date and page number—into a CSV format for efficient access and analysis.

### Key Features

- Image Processing: Accepts property deed images in TIFF format.
- Content Analysis: Employs text recognition and analysis algorithms to detect racist language.
- Data Extraction: Automates the extraction of deed date and page number for each document analyzed.

Our aim is to assist the Longmeadow Historical Society in their efforts to document and understand historical injustices, contributing to a broader societal recognition and rectification of past discriminations.

## Requirements
Install essential libraries:
```
pip install -r requirements.txt
```

## Set up OpenAI_API_KEY
In folder `modules`: 

1. Duplicate the file `env.template`

2. Add your `api key` and `organization id` to `OPENAI_API_KEY` and `OPENAI_ORG_ID`. You can get your api key and organization ID via the link: (api-keys)[https://platform.openai.com/api-keys], 
(organization)[https://platform.openai.com/account/organization]

3. Rename this file to `.env`

   
## Quick Start
In file `main.py`, change the folder path to your path(line 24).

Then in command line, run:
```
python main.py
```
