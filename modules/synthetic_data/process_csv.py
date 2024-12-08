import os
import re



def retrieve_csv(path):
    #open file
    with open(path, "r", encoding="utf-8") as file:
        csv_content = file.read()
    
    #get rid of extraneous characters, split by line, remove duplicates
    csv_content = csv_content.replace("\"","")
    csv_content = csv_content.split("\n")
    csv_content = set(csv_content)
    
    return csv_content

def retrieve_all_csvs():
    mn_counties = ['washington', 'olmsted', 'dakota']
    res = []
    for county in mn_counties:
        path = f'modules/synthetic_data/more_racist_deeds/covenants-mn-{county}-county-cleaned.csv'
        res += retrieve_csv(path)
    return res

print(len(retrieve_all_csvs()))

    