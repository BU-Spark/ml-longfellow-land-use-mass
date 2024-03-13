import re

def locate(ocr_text):
    # input: string produced by the ocr
    # output: (1) array of possible page numbers (may include false positives)
    #         (2) array of possible dates
    possible_pages = []
    possible_dates = []
    result = ocr_text.split("\n")
    pattern = r'Re(?:c\'d\.|ceived|e\'d\.)'
    for word in result:
        # checks for possible page numbers
        if word.isdigit() == True:
            possible_pages.append(word)
        # checks for rec'd dates
        if re.match(pattern, word):
            # appending entire string for human judgement as OCR fails to correctly translate years in few cases
            possible_dates.append(word)
    if not possible_pages:
        possible_pages.append("Null")
    if not possible_dates:
        possible_dates.append("Null")
    return possible_pages, possible_dates