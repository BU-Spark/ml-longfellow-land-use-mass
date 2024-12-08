import os
import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

class BatchProcessor:
    def __init__(self):
        self.client = OpenAI(
            api_key=os.getenv("OPENAI_API_KEY"),
            organization=os.getenv("OPENAI_ORG_ID")
        )
    
    def prepare_batch(self, folder_path, output_file):
        """Prepare a batch input file from a folder of text files."""
        with open(output_file, "w") as out_file:
            for filename in os.listdir(folder_path):
                if filename.endswith(".txt"):
                    file_path = os.path.join(folder_path, filename)
                    with open(file_path, "r") as file:
                        text = file.read()

                    batch_entry = {
                        "custom_id": filename,
                        "method": "POST",
                        "url": "/v1/chat/completions",
                        "body": {
                            "model": "gpt-4o-mini",
                            "messages": [
                                {
                                    "role": "system",
                                    "content": (
                                        "You are a helpful assistant designed to check if there's any racial content. "
                                        "Please review this document for any racial or discriminatory expressions. "
                                        "If yes, return 'Yes'; if there's none, please return 'No racial content found'. "
                                        "If there is any doubt or ambiguity, assume the text contains racial content and respond 'Yes'."
                                    )
                                },
                                {"role": "user", "content": text}
                            ],
                            "max_tokens": 1000
                        }
                    }
                    out_file.write(json.dumps(batch_entry) + "\n")
        print(f"Batch file created: {output_file}")

    def upload_batch_file(self, batch_file_path):
        """Upload the prepared batch input file."""
        with open(batch_file_path, "rb") as f:
            batch_input_file = self.client.files.create(
                file=f,
                purpose="batch"
            )
        print(f"Batch input file uploaded. File ID: {batch_input_file.id}")
        return batch_input_file.id

    def create_batch(self, file_id):
        """Create a batch job with the uploaded input file."""
        batch = self.client.batches.create(
            input_file_id=file_id,
            endpoint="/v1/chat/completions",
            completion_window="24h",
            metadata={
                "description": "Deed analysis batch"
            }
        )
        print(f"Batch created. Batch ID: {batch.id}")
        return batch.id

    def check_batch_status(self, batch_id):
        """Check the status of a batch job."""
        batch_status = self.client.batches.retrieve(batch_id)
        print(f"Batch Status: {batch_status.status}")
        if batch_status.status == "completed":
            output_file_id = batch_status.output_file_id
            print(f"Output File ID: {output_file_id}")
            return output_file_id
        else:
            return None

    def retrieve_results(self, output_file_id, output_path):
        """Retrieve the results of a completed batch job."""
        file_response = self.client.files.content(output_file_id)
        with open(output_path, "wb") as out_file:
            out_file.write(file_response.read())
        print(f"Batch results downloaded to {output_path}")

os.system('ls')

if __name__ == "__main__":
    processor = BatchProcessor()

    folder_path = "./racist"  
    batch_input_file = "batch_input.jsonl"
    batch_output_file = "batch_output.jsonl"

    # Step 1: Prepare the batch input file
    processor.prepare_batch(folder_path, batch_input_file)

    # Step 2: Upload the batch input file
    file_id = processor.upload_batch_file(batch_input_file)

    # Step 3: Create a batch job
    batch_id = processor.create_batch(file_id)

    # Step 4: Poll for batch status
    import time
    while True:
        output_file_id = processor.check_batch_status(batch_id)
        if output_file_id:
            break
        print("Batch not complete. Retrying in 30 minutes...")
        time.sleep(180)

    # Step 5: Retrieve the results
    processor.retrieve_results(output_file_id, batch_output_file)