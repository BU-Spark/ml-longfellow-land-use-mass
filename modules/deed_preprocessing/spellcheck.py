import language_tool_python

# Initialize the LanguageTool instance for English
tool = language_tool_python.LanguageTool('en-US')

def correct_spelling(text):
    """Correct spelling and grammar errors in the given text using LanguageTool."""
    
    # Check the text using LanguageTool
    matches = tool.check(text)
    
    # Apply the suggested corrections from LanguageTool
    corrected_text = language_tool_python.utils.correct(text, matches)
    
    return corrected_text