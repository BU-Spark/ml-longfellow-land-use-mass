# Synthetic Data Module

During the project we lacked ground truth to create a classifier capable of differentiating on racist language. To get around this, we borrowed racist covenant clauses from other studies (data in the more_racist_deeds) directory. We then injected them into our own clauses to create racist versions of our non-racist data. Note that BoW vectorization does not take into account word ordering, so the clause can be injected anywhere.

## inject_racism.py

Enumerates through an input directory of OCRed deed text on the SCC and injects a racist clause using this loop:

```python
for i, string in enumerate(strings):
        selected_file = random.choice(text_files)
        input_path = os.path.join(input_directory, selected_file)
        
        with open(input_path, 'r') as file:
            content = file.read()
        
        doc = nlp(content)
        sentences = [sent.text for sent in doc.sents]
        
        middle_index = len(sentences) // 2
        sentences.insert(middle_index, string)
        
        modified_content = ' '.join(sentences)
        output_path = os.path.join(output_directory, f"RACIST_{i}_{selected_file}")
        with open(output_path, 'w') as file:
            file.write(modified_content)
        
        print(f"Saved modified file: {output_path}")
```

Stores all newly racist text files in a directory called synthetic_data/

## train_model.py

- Combines our actual racist ground truth and synthetic racist ground truth into a data frame, and marks all other deeds as non-racist.
- Performs a train test split on the dataset, and trains a logistic regression model.
- "False positives" would be deeds with an unknown class that we marked as non-racist, yet our model said is racist based on its training, so it may actually be a truly racist new deed.
- Misclassified texts are stored in a separate directory for manual examination:

```python
for idx in misclassified_indexes:
    text = preprocessed_data.loc[idx, 'original_text']
    is_racist = y_test.loc[idx]
    predicted = y_pred[X_test.index.get_loc(idx)]

    filename = f"{misclassified_dir}/misclassified_{idx}_actual_{is_racist}_pred_{predicted}.txt"
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)

print(f'Saved {len(misclassified_indexes)} misclassified texts to {misclassified_dir}')
```

This script should be run in the SCC, with the non-racist ground truth path pointing to all OCRed deeds.