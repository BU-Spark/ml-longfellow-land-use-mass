import os
import pandas as pd
from bigotry_dict import bigotry_dict  

def count_keywords_in_text(text, bigotry_dict):
    keyword_counts = {}
    text_lower = text.lower()  # Normalize the text to lowercase

    for keyword in bigotry_dict:
        keyword_lower = keyword.lower()  # Normalize the keyword to lowercase
        if keyword_lower in keyword_counts:
            continue  # Skip if this keyword has already been processed

        count = text_lower.count(keyword_lower)  # Count keyword occurrences
        if count > 0:
            keyword_counts[keyword_lower] = {'count': count, 'texts': [text], 'display_keyword': keyword}
    
    return keyword_counts

def save_racist_deed(text, deed_id, output_dir="racist_deeds"):
    """Saves the deed text to a txt file if racist keywords are found."""
    os.makedirs(output_dir, exist_ok=True)  # Create output directory if it doesn't exist
    
    file_path = os.path.join(output_dir, f"deed_{deed_id}.txt")
    with open(file_path, 'w') as f:
        f.write(text)
    
    print(f"Deed saved to: {file_path}")

# Aggregate keyword counts and check for racist deeds in all text objects
def process_deeds(text_objects):
    total_keyword_counts = {}

    for i, text_obj in enumerate(text_objects):
        keyword_counts = count_keywords_in_text(text_obj['original_text'], bigotry_dict)
        
        racist_deed = False
        for keyword_lower, data in keyword_counts.items():
            if data['count'] > 0:
                racist_deed = True  # Mark deed as racist if any keyword is found
                if keyword_lower not in total_keyword_counts:
                    total_keyword_counts[keyword_lower] = {'count': 0, 'texts': [], 'display_keyword': data['display_keyword']}
                total_keyword_counts[keyword_lower]['count'] += data['count']
                total_keyword_counts[keyword_lower]['texts'].extend(data['texts'])  # Collect texts

        # If any racist keyword is found, save the deed text
        if racist_deed:
            save_racist_deed(text_obj['original_text'], i)

    # Convert the total counts to a pandas DataFrame for easier analysis
    keyword_df = pd.DataFrame([(data['display_keyword'], data['count'], data['texts']) 
                               for data in total_keyword_counts.values()], 
                              columns=['Keyword', 'Count', 'Texts'])

    # Sort keywords by count for analysis
    keyword_df_sorted = keyword_df.sort_values(by="Count", ascending=False)

    # Display the dataframe for analysis (texts associated with each keyword)
    print(keyword_df_sorted)

# Example usage
text_objects = [
    {"original_text": "This deed restricts African Americans and Chinese people."},
    {"original_text": "This is a deed allowing Italian and Chinese immigrants."},
    {"original_text": "This is a regular deed with no discriminatory language."}
]

# Process the deeds and save any racist ones
process_deeds(text_objects)
