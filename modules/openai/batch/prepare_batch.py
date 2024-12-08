import os
import json

def prepare_batch(folder_path, output_file):
    with open(output_file, "w") as out_file:
        for filename in os.listdir(folder_path):
            if filename.endswith(".txt"):
                file_path = os.path.join(folder_path, filename)
                
                # Read the content of the file
                with open(file_path, "r") as file:
                    text = file.read()
                
                # Create a batch entry
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

if __name__ == "__main__":
    prepare_batch("folder_of_deeds", "batch_input.jsonl") # add folder of deeds to pass into openai
