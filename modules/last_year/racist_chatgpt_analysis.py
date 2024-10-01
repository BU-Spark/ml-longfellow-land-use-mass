from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(
  organization=os.getenv('OPENAI_ORG_ID'),
  api_key=os.getenv('OPENAI_API_KEY')
)

def racist_chatgpt_analysis(text):
    response = client.chat.completions.create(
      model="gpt-3.5-turbo-0125",
      messages=[ # prompt engineering
        {"role": "system", "content": "You are a helpful assistant designed to check if there's any racial contents. \
                                       Please review this document for any racial or discriminatory expressions. \
                                       If yes, return 'Yes', if there's none, please return 'No racial content found'."},
        {"role": "user", "content": text}
      ]
    )
    if response.choices[0].message.content == "Yes":
      return True
    else:
      return False