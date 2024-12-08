from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

def upload_batch_file(batch_file_path):
    client = OpenAI(
        api_key=os.getenv("OPENAI_API_KEY"),
        organization=os.getenv("OPENAI_ORG_ID")
    )

    with open(batch_file_path, "rb") as f:
        batch_input_file = client.files.create(
            file=f,
            purpose="batch"
        )

    print(f"Batch input file uploaded. File ID: {batch_input_file.id}")
    return batch_input_file.id

if __name__ == "__main__":
    upload_batch_file("batch_input.jsonl")
