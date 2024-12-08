from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

def list_batches(limit=10):
    client = OpenAI(
        api_key=os.getenv("OPENAI_API_KEY"),
        organization=os.getenv("OPENAI_ORG_ID")
    )

    batches = client.batches.list(limit=limit)
    for batch in batches.data:
        print(f"Batch ID: {batch.id}, Status: {batch.status}")

if __name__ == "__main__":
    list_batches()
