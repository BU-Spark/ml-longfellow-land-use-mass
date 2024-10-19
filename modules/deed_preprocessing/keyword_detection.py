import re

def detect_racist_language_with_dict(preprocessed_text, bigotry_dict):
    # Convert text to lowercase to make the search case-insensitive
    text_lower = preprocessed_text.lower()
    detected_keywords = {}

    # Loop through the dictionary keys (keywords)
    for keyword in bigotry_dict:
        # Search for the keyword in the text using case-insensitive matching
        if re.search(rf'\b{keyword.lower()}\b', text_lower):
            # Count how many times the keyword appears
            count = len(re.findall(rf'\b{keyword.lower()}\b', text_lower))
            detected_keywords[keyword] = count

    return detected_keywords
