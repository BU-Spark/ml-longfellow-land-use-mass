from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

def check_batch_status(batch_id):
    client = OpenAI(
        api_key=os.getenv("OPENAI_API_KEY"),
        organization=os.getenv("OPENAI_ORG_ID")
    )

    batch_status = client.batches.retrieve(batch_id)
    print(f"Batch Status: {batch_status.status}")

    if batch_status.status == "completed":
        output_file_id = batch_status.output_file_id
        print(f"Output File ID: {output_file_id}")
        return output_file_id
    else:
        print(f"Batch Status: {batch_status.status}")
        return None

if __name__ == "__main__":
    batch_id = "" # batch id here
    check_batch_status(batch_id)
