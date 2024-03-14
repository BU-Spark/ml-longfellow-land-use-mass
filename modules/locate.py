import re

def locate(ocr_text):
    # input: string produced by the ocr
    # output: (1) array of possible page numbers (may include false positives)
    #         (2) array of possible dates
    #         (3) array of possible book numbers 
    possible_pages = []
    possible_dates = []
    possible_book = []
    result = ocr_text.split("\n")
    pattern = re.compile(r'Re(?:c|ceived|e|o|a)')
    book_pattern = re.compile(r'B(?:OOK|00K)',  re.IGNORECASE)
    for word in result:
        # checks for possible page numbers
        if word.isdigit() == True:
            possible_pages.append(word)
        # checks for rec'd dates
        if re.match(pattern, word):
            # appending entire string for human judgement as OCR fails to correctly translate years in few cases
            possible_dates.append(word)
        if re.match(book_pattern, word):
            possible_book.append(word)
    if not possible_pages:
        possible_pages.append("Null")
    if not possible_dates:
        possible_dates.append("Null")
    if not possible_book:
        possible_book.append("Null")
    return possible_pages, possible_dates, possible_book