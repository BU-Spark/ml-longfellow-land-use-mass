import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.organization = os.getenv('OPENAI_ORG_ID')
openai.api_key = os.getenv('OPENAI_API_KEY')

def racist_chatgpt_analysis(text):
    try:
        response = openai.ChatCompletion.create(
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
        )
        if response.choices[0].message.content.strip() == "Yes":
            return True
        else:
            return False
    except Exception as e:
        print(f"Error: {e}")
        return False