import os
import pandas as pd
from pathlib import Path
import sys
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
sys.path.append('../deed_preprocessing')
from preprocessor import preprocess_text

def preprocess_bag_of_words(preprocessed_text_list):
    texts = [preprocessed["original_text"] for preprocessed in preprocessed_text_list]
    
    vectorizer = CountVectorizer()
    bag_of_words = vectorizer.fit_transform(texts)

    bow_df = pd.DataFrame(bag_of_words.toarray(), columns=vectorizer.get_feature_names_out())

    return bow_df

def preprocess_deeds():
    sys.path.append('../deed_preprocessing')
    from preprocessor import preprocess_text

    racist_dir = Path('./racist_deeds_text')
    non_racist_dir = Path('./non_racist_deeds_text')

    all_data = pd.DataFrame()

    def process_directory(directory, is_racist_label):
        nonlocal all_data
        for file in directory.iterdir():
            if file.is_file() and file.suffix == '.txt':
                with file.open('r', encoding='utf-8') as f:
                    text = f.read()
                    processed_text = preprocess_text(text)

                    df = pd.DataFrame([processed_text])
                    df['is_racist'] = is_racist_label

                    all_data = pd.concat([all_data, df], ignore_index=True)

    process_directory(racist_dir, 1)
    # process_directory(non_racist_dir, 0)

    return all_data

if __name__ == "__main__":
    preprocessed_data = preprocess_deeds()
    texts = preprocessed_data['original_text']
    preprocessed_text_list = texts.apply(preprocess_text).tolist()
    bow_df = preprocess_bag_of_words(preprocessed_text_list)
    
    X = bow_df
    y = preprocessed_data['is_racist']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    logistic_model = LogisticRegression(max_iter=1000)
    logistic_model.fit(X_train, y_train)
    y_pred = logistic_model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    print(f"Accuracy: {accuracy:.2f}")
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))
