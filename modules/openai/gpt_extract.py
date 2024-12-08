import os
import openai
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

folder_path = "racist_deeds_text"

output_csv = "deed_names_locations.csv"

data = []

def extract_names_and_locations(text):
    """
    Extract names and locations from text using OpenAI.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are an assistant that extracts names and locations from legal text. "
                        "For the given input, identify all names of people (grantors, grantees) and "
                        "locations (addresses, city, county, state). "
                        "Return the names as a comma-separated list and locations as a separate comma-separated list "
                        "strictly in the format:\nNames: [comma-separated names]\nLocations: [comma-separated locations]."
                    )
                },
                {"role": "user", "content": text}
            ]
        )
        output = response.choices[0].message.content.strip()

        names, locations = "", ""

        for line in output.split("\n"):
            if line.startswith("Names:"):
                names = line.replace("Names:", "").strip()
            elif line.startswith("Locations:"):
                locations = line.replace("Locations:", "").strip()
                
        return names, locations
    except Exception as e:
        print(f"Error extracting names and locations: {e}")
        return "", ""

for filename in os.listdir(folder_path):
    if filename.endswith(".txt"):
        file_path = os.path.join(folder_path, filename)
        
        with open(file_path, "r") as file:
            text = file.read()
        
        names, locations = extract_names_and_locations(text)
        
        data.append({"Filename": filename, "Names": names, "Locations": locations})
        print(f"Processed {filename}")

df = pd.DataFrame(data)
df.to_csv(output_csv, index=False)
print(f"Results saved to {output_csv}")