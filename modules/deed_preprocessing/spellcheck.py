from spellchecker import SpellChecker

# Initialize the spellchecker
spell = SpellChecker()

def correct_spelling(text):
    """Correct spelling errors in the given text and return corrected text."""
    
    words = text.split()
    # Correct each word in the text
    corrected_words = []
    for word in words:
        if spell.unknown([word]):
            candidates = spell.candidates(word)
            # Check if candidates is not None and has items
            if candidates:
                corrected_word = next(iter(candidates))  # Use the first candidate
            else:
                corrected_word = word  # Keep the original word if no candidates
        else:
            corrected_word = word
        corrected_words.append(corrected_word)

    # Join corrected words back into a single string
    corrected_text = ' '.join(corrected_words)
    
    return corrected_text
