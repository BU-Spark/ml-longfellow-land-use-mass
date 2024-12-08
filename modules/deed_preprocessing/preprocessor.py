import re
import spacy
from collections import Counter

nlp = spacy.load('en_core_web_sm')

def preprocess_text(text):
    text = re.sub(r'[\n\r\t]', ' ', text)
    text = re.sub(r'[^\x00-\x7F]+', '', text)
    doc = nlp(text)
    
    result = {
        "original_text": text,
        "sentences": [],
        "pos_groups": {},
        "named_entities": [],
        "dependencies": [],
        "token_offsets": [],
        "word_frequency": {},
        "sentence_lengths": [],
        "pos_counts": {}
    }
    
    pos_groups = {
        "NOUN": [], "VERB": [], "ADJ": [], "ADV": [], "PROPN": [],
        "DET": [], "AUX": [], "PRON": [], "ADP": [], "NUM": [],
        "PART": [], "PUNCT": [], "INTJ": [], "X": []
    }
    
    all_tokens = []
    
    for sent in doc.sents:
        result["sentences"].append(sent.text)
        result["sentence_lengths"].append(len(sent))
        
        for token in sent:
            pos = token.pos_
            all_tokens.append(token.text)
            
            if pos in pos_groups:
                pos_groups[pos].append(token.text)
                
            result["dependencies"].append({
                "token": token.text,
                "dep": token.dep_,
                "head": token.head.text
            })
            result["token_offsets"].append({
                "token": token.text,
                "start": token.idx,
                "end": token.idx + len(token.text)
            })
    
    result["pos_groups"] = pos_groups
    result["named_entities"] = [{"text": ent.text, "label": ent.label_} for ent in doc.ents]
    result["word_frequency"] = dict(Counter(all_tokens))
    result["pos_counts"] = dict(Counter([token.pos_ for token in doc]))

    result["names"] = [ent.text for ent in doc.ents if ent.label_ == "PERSON"]
    result["locations"] = [ent.text for ent in doc.ents if ent.label_ in {"GPE", "LOC"}]
    
    return result