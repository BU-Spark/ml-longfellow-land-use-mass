# OpenAI module

# Steps to setup OpenAI api

    1. Go to https://platform.openai.com/docs/overview and login using the email that Spark invited.
    2. Go to settings and in the general tab, get the Organization ID
    3. Next go to the api key tab and select create new secret key and create it
    4. Add your api key and org id into .env 
        OPENAI_API_KEY=
        OPENAI_ORG_ID=

## racist_chatgpt_analysis.py

Makes a call to chatgpt. 

The model and prompt used is:

```python
model="gpt-4o-mini",
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant designed to check if there's any racial contents. \
                        Please review this document for any racial or discriminatory expressions. \
                        If yes, return 'Yes', if there's none, please return 'No racial content found'. \
                        If there is any doubt or ambiguity, assume the text contains racial content and respond 'Yes'."
        },
        {"role": "user", "content": text}
    ]
```

Output of each call is a Yes or No racial content found. 

## batch

The batch folder contains all the necessary steps to call gpt-4o-mini in batches. Each batch call has a completion window of 24 hours, but the cost is 50% off. 

The main batch call file is batch_preprocessing.py. It needs to have a folder path specified to make the call.



