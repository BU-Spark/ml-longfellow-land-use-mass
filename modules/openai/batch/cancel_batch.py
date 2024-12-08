from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

def cancel_batch(batch_id):
    client = OpenAI(
        api_key=os.getenv("OPENAI_API_KEY"),
        organization=os.getenv("OPENAI_ORG_ID")
    )

    client.batches.cancel(batch_id)
    print(f"Batch {batch_id} cancelled.")

if __name__ == "__main__":
    batch_id = "" # batch id here obtained from create_batch.py
    cancel_batch(batch_id)
