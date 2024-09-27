# Technical Project Document Template
**Nathaniel Quisel, Jacob Stein, Jianying Liu, 2024-September-24 vx.x.x-dev**

## Overview
The Racist Deeds Project aims to expand the identification of property deeds with racist restrictions, initially focusing on Longmeadow, Massachusetts. These restrictions, targeting marginalized groups like African Americans, were outlawed by the Fair Housing Act of 1968 and locally in Massachusetts by 1946. This project seeks to streamline the identification process of discriminatory deeds to support the Longmeadow Historical Society.

The focus of this semester is to build a data pipeline that will interact with deeds stored in a designated Google Drive location and potentially adjust some of the Gen AI prompts. The project will implement Optical Character Recognition (OCR) tools via a Python package to digitize and extract text from scanned deed documents, which will facilitate more efficient analysis and pattern recognition. Additionally, there will be an effort to refine and adjust the Gen AI prompts to improve the mapping.

## A. Human Actions for Automation
Normally, the process of parsing thousands of deeds for racist language would take a long time for humans to achieve. The process would involve:
- **Data Sources**: Compile deeds from Longmeadow, Massachusetts from various sources into a comprehensive database
- **Data Extraction**: Manually read each deed
- **Data Transformation**: Identify patterns or sections within the deeds that contain racist language, either explicitly or implicitly
- **Data Compilation**: compile a repository of racist deeds and their associated metadata for further analysis

## B. Problem Statement

- **Automated Data Collection**: Develop scripts to compile deeds into a database.
- **Optical Character Recognition (OCR)**: Utilize OCR to automatically read and digitize text from deeds. This can involve:
  - **Batch Processing**: Process multiple scanned documents using parallel OCR engines
  - **Quality Control**: Implement checks to ensure the accuracy of the extracted text, flagging any documents requiring review.
  - **Specialized Models**: There are specialized models and frameworks, both pre-trained and otherwise, for recognizing text in historical documents; examples include Kraken OCR and Pylaia.
  - **Existing Cloud Tools**: With guidance from the instructor, Google Cloud OCR and Microsoft Azure OCR will probably be better than what is trainable in a semester, so these tools must be tested on written documents.
- **Pattern Recognition**: Implement machine learning models to identify patterns or sections within the extracted deeds that contain racist language. This can include:
  - **Feature Extraction**: Extract features indicative of racist language (e.g., specific words or phrases).
  - **Classification**: Train models to classify sections of deeds as containing racist language or not.
  - **Parallel Model Training**: Use different algorithms for hyperparameter tuning processes in parallel to identify the best performing model.
- **Automated Metadata**: Once the model identifies potentially racist deeds, automatically compile a repository that includes:
  - The deed text.
  - Metadata (e.g., date, property owner, geographic location).
  - Classification results (e.g., whether it contains racist language).

## C. Checklist for Project Completion
- **Sponsor Kickoff**: Review deed data, set up communication channels.
- **Benchmarking**: Define success metrics for OCR and classification.
- **Solution Summary**: Mock analysis with OCR and ML tool results.
- **Exploratory Analysis**: Identify patterns in deed data.
- **Visualization**: Create and refine visualizations for deed analysis results.
- **Final Presentation**: Present findings and tool effectiveness to sponsor.

## D. Path to Operationalization
- User can input new deeds and site will identify if there is racist language
- Site will be able to process old fashioned texts and convert it to text
- Metadata such as location, date, property owner will be identified
- Specific phrasing that led to the identification as racist can be output
- Google Cloud OCR, Microsoft Azure OCR, Llama, OpenAI API are all technologies we expect to utilize

## Resources
- [Google Cloud OCR Documentation](https://cloud.google.com/use-cases/ocr)
- [Microsoft Azure OCR Documentation](https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/overview-ocr)
- [Pytesseract Documentation](https://pytesseract.readthedocs.io/en/latest/)
- [Kraken OCR Documentation](https://kraken.re/main/index.html)
- [PyLaia Documentation](https://github.com/jpuigcerver/PyLaia)

## Data Sets
- [Hampden Deeds Search Engine](https://search.hampdendeeds.com/ALIS/WW400R.HTM?WSIQTP=LR01D&WSKYCD=N)
- [All deeds](https://drive.google.com/drive/folders/1V9x-24SeIQlAyOeVQRXbRElQaw_ig6il?usp=sharing)
- [Deeds labeled as containing racist language](https://github.com/BU-Spark/pitne-land-use-mass/blob/main/Database%20of%20Racist%20Deeds%20-%20Discriminated_Group_Deeds.csv)

## References
Weekly Meeting Updates
9/23/24 - Initial meeting with the PM to discuss the objectives of the project
