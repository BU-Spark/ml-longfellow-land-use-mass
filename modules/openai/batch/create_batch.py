from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

def create_batch(file_id):
    client = OpenAI(
        api_key=os.getenv("OPENAI_API_KEY"),
        organization=os.getenv("OPENAI_ORG_ID")
    )

    batch = client.batches.create(
        input_file_id=file_id,
        endpoint="/v1/chat/completions",
        completion_window="24h",
        metadata={
            "description": "Deed analysis batch"
        }
    )

    print(f"Batch created. Batch ID: {batch.id}")
    return batch.id

if __name__ == "__main__":
    file_id = "" # file id here obtained from running upload_batch_file.py
    create_batch(file_id)
