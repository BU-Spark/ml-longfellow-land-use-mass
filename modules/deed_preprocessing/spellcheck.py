import language_tool_python
from autocorrect import Speller

# Initialize the LanguageTool instance for English
tool = language_tool_python.LanguageTool('en-US')

# Initialize the Speller instance from autocorrect
spell = Speller(lang='en')

def correct_spelling(text):
    """Correct spelling using Autocorrect, then fix grammar using LanguageTool."""
    
    # Step 1: Correct basic spelling errors using Autocorrect
    auto_corrected_text = spell(text)
    
    # Step 2: Check the autocorrected text using LanguageTool for grammar and style errors
    matches = tool.check(auto_corrected_text)
    
    # Step 3: Apply the suggested corrections from LanguageTool
    final_corrected_text = language_tool_python.utils.correct(auto_corrected_text, matches)
    
    return final_corrected_text
