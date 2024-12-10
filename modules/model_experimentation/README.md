# Model Experimentation Module

This module contains code from when we began experimenting with new models.

## create_df.py

This code assumes the existence of a racist_deeds_text and non_racist_deeds_text directory, which you can form using read_tiffs.py in deed_preprocessing.

The code then preprocesses all deeds in either directory and adds the correct class label using this function:

```python
def process_directory(directory, is_racist_label):
        nonlocal all_data, racist_count, non_racist_count
        for file in directory.iterdir():
            if file.is_file() and file.suffix == '.txt':
                with file.open('r', encoding='utf-8') as f:
                    text = f.read()
                    processed_text = preprocess_text(text)

                    df = pd.DataFrame([processed_text])
                    df['is_racist'] = is_racist_label

                    all_data = pd.concat([all_data, df], ignore_index=True)

                if is_racist_label == 1:
                    racist_count += 1
                else:
                    non_racist_count += 1
```

The output will be a structured dataframe with the correct classes

## bag_of_words_logistic_regression.py

Uses a bag of words vectorizer on the dataframe from create_df, and runs it through a train test split, using sklearn's vectorizer and logistic regression functions:

```python
bow_df, vectorizer = preprocess_bag_of_words(preprocessed_text_list)
    
    X = bow_df
    y = preprocessed_data['is_racist']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    logistic_model = LogisticRegression(max_iter=1000)
    logistic_model.fit(X_train, y_train)
```