import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, roc_curve, auc
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)
import pickle

def preprocess_bag_of_words(preprocessed_text_list):
    texts = [preprocessed["original_text"] for preprocessed in preprocessed_text_list]
    
    vectorizer = CountVectorizer()
    bag_of_words = vectorizer.fit_transform(texts)

    bow_df = pd.DataFrame(bag_of_words.toarray(), columns=vectorizer.get_feature_names_out())

    return bow_df, vectorizer

if __name__ == "__main__":
    preprocessed_data = pd.read_pickle('preprocessed_deeds.pkl')

    texts = preprocessed_data['original_text']
    preprocessed_text_list = texts.apply(lambda x: {"original_text": x}).tolist()
    
    bow_df, vectorizer = preprocess_bag_of_words(preprocessed_text_list)
    
    X = bow_df
    y = preprocessed_data['is_racist']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    logistic_model = LogisticRegression(max_iter=1000)
    logistic_model.fit(X_train, y_train)

    # Save the model and vectorizer
    with open('vectorizer.pkl', 'wb') as vec_file:
        pickle.dump(vectorizer, vec_file)
    with open('logistic_model.pkl', 'wb') as model_file:
        pickle.dump(logistic_model, model_file)

    y_pred = logistic_model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    print(f"Accuracy: {accuracy:.2f}")
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))

    conf_matrix = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(6, 4))
    sns.heatmap(conf_matrix, annot=True, fmt="d", cmap="Blues", xticklabels=['Non-racist', 'Racist'], yticklabels=['Non-racist', 'Racist'])
    plt.title('Confusion Matrix')
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.show()

    y_prob = logistic_model.predict_proba(X_test)[:, 1]
    fpr, tpr, _ = roc_curve(y_test, y_prob)
    roc_auc = auc(fpr, tpr)
    
    plt.figure(figsize=(6, 4))
    plt.plot(fpr, tpr, label=f'ROC curve (AUC = {roc_auc:.2f})')
    plt.plot([0, 1], [0, 1], 'k--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver Operating Characteristic (ROC) Curve')
    plt.legend(loc="lower right")
    plt.show()

    feature_importance = pd.Series(logistic_model.coef_[0], index=vectorizer.get_feature_names_out())
    top_features = feature_importance.nlargest(10)
    
    plt.figure(figsize=(8, 6))
    top_features.plot(kind='barh', color='skyblue')
    plt.title('Top 10 Most Influential Words for Racist Classification')
    plt.xlabel('Coefficient Value')
    plt.ylabel('Word')
    plt.show()

# Function to make predictions based on the trained model
def predict(processed_text, vectorizer, logistic_model):
    bow_text = vectorizer.transform([processed_text["original_text"]])
    prediction = logistic_model.predict(bow_text)
    return {
        'is_racist': bool(prediction[0]),
    }