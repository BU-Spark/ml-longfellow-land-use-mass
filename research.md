## Papers

### Paper 1 - Racism Detection by Analyzing Differential Opinions Through Sentiment Analysis of Tweets Using Stacked Ensemble GCR-NN Model

- [Source](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=968489)
- Study aims to analyze racist tweets using sentiment analysis related to racism.
- Overt and covert racism is rampant on Twitter, making it an excellent sample space for training a racism classification model.
- Study used a stacked ensemble model called Gated Convolutional Recurrent-Neural Network, which uses GRU, CNN, and RNN.
- Used a dataset of 169,999 tweets with racist keywords over a period of 10 days, annotated using TextBlob to classify sentiment.
- Used NLP techniques - tokenization, lemmatization, and stop word exclusion.
- Tweets were classified by polarity, with negative sentiment indicating racism.
- Used Term Frequency-Inverse Document Frequency and Bag of Words for extracting features for training.
- GCR-NN outperformed machine learning models like SVM and KNN, and standalone deep learning models.
- 97% accuracy for racist tweets, showing superior performance and accuracy.
- Ensemble deep learning models are good for detecting racist sentiment.

### Paper 2 - Data Capture Automation in the South African Deeds Registry using Optical Character Recognition (OCR)

- [Source](https://open.uct.ac.za/server/api/core/bitstreams/e1024f88-91c0-465a-9830-2c85a8807da6/content)
- Article explores how OCR can help reduce the backlog in registering title deeds in South Africa.
- South Africa's backlog consists of nearly 900,000 unregistered deeds due to inefficiencies in manual processes.
- Study proposes an OCR pipeline using Tesseract for typed text recognition and IPFS for securing the data.
- Pipeline achieved an accuracy rate of 89.6%, excelling in extracting typed text.
- System struggled with recognizing handwritten and stamped entries, which affected its overall performance.
- Based on these challenges, further improvements are recommended to enhance handling of various input types.
- OCR solution processes more deeds per day compared to manual methods, improving overall efficiency.
- Implementation of OCR could significantly reduce the backlog and improve the Deeds Registry process.
- IPFS is used to secure the extracted data, ensuring protection of sensitive information.
- Study concludes that OCR, despite needing improvements, can enhance the efficiency of deed registration and address the backlog issue.

### Paper 3 - Documenting Racially Restrictive Covenants in 20th Century Philadelphia

- [Source](https://www.jstor.org/stable/26967201)
- Concerns use of racially restrictive covenants in property deeds in Philadelphia between 1920 and 1932.
- Covenants were designed to prevent African Americans from owning or occupying certain properties, reinforcing segregation and racial inequality.
- Study used OCR to automate the identification of these covenants in deed records.
- Created a spatial database to analyze patterns of racial segregation and its effects on property values and neighborhood demographics.
- Project processed over a million scanned deed images, converting them into searchable text using OCR.
- Focused on keywords like "Caucasian" and "Negro" to detect racially restrictive language in the deeds.
- OCR software was configured with pre-processing tools to enhance detection of these discriminatory covenants.
- Despite facing challenges with image quality, OCR enables efficient analysis of large volumes of historical records.
- The use of OCR drastically reduces the manual workload required to search through deed archives.
- Study highlights the effectiveness of OCR in studying historical patterns of segregation and its lasting impact on cities like Philadelphia.

## Open Source Project

### RoBERTa
- [Source](https://github.com/facebookresearch/fairseq/tree/main/examples/roberta)
- [HuggingFace](https://huggingface.co/docs/transformers/en/model_doc/roberta#overview)
- Fine-tuned BERT model from Facebook AI.
- Might require specialized training on some existing racist deeds.
- Can be used for various NLP tasks like text classification, sequence tagging, and sentiment analysis.
- Supports integration with Hugging Face Transformers for quick model deployment.
- Useful for transfer learning applications where limited labeled data is available.

### Automatic hate tweet detection
- [Source](https://github.com/datascisteven/Automated-Hate-Tweet-Detection)
- A Python-based project for automating the detection of hate speech on Twitter.
- Uses a pre-trained transformer model to classify tweets as hate speech or not.
- Provides a real-time sentiment detection pipeline with tokenization and preprocessing of tweets.
- Features visualizations for analyzing hate speech trends across time and geolocation.

### Detecting Hate Speech with GPT-3
- [Source](https://github.com/kelichiu/GPT3-hate-speech-detection)
- Utilizes OpenAI’s GPT-3 to detect hate speech, particularly sexist and racist content.
- Includes sample notebooks for testing GPT-3 on hate speech datasets.
- Offers customization for applying different thresholds to flag hate speech depending on the use case.
- Can be integrated with social media platforms or content moderation systems.
