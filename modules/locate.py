import re

def locate(ocr_text):
    # input: string produced by the ocr
    # output: (1) array of possible page numbers (may include false positives)
    #         (2) array of possible dates
    possible_pages = []
    possible_dates = []
    result = ocr_text.split("\n")
    pattern1 = r'Ree\'d\. (\w+\. \d{1,2}, \d{4})'
    pattern2 = r'Rec\'d\. (\w+\. \d{1,2}, \d{4})'
    for word in result:
        # checks for possible page numbers
        if word.isdigit() == True:
            possible_pages.append(word)
        # checks for rec'd dates
        if re.match(pattern1, word):
            possible_dates.append(re.match(pattern1, word).group(1))
        elif re.match(pattern2, word):
            possible_dates.append(re.match(pattern2, word).group(1))
    return possible_pages, possible_dates