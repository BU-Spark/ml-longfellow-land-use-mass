import os
import re

def retrieve_html():
    #open file
    with open("more_racist_deeds/seattle-covenants.html", "r", encoding="utf-8") as file:
        html_content = file.read()

    #create regex patterns for both cases
    pattern1 = r"<td class=xl70 width=330>(.*?)</td>"
    pattern2 = r"<td class=xl70 width=330\n  x:str=\"(.*?)\""

    #filter by pattern
    matches1 = re.findall(pattern1, html_content)
    matches2 = re.findall(pattern2, html_content)

    #matches1 needs additional cleaning of extraneous phrases
    substrings_to_remove = ["&quot;", "&nbsp;"]

    final = []
    for match in matches1:
        current = match
        for substring in substrings_to_remove:
            current = current.replace(substring, "")
        final.append(current)

    final = [s for s in final if s != ""]

    #add matches2
    for match in matches2:
        final.append(match)

    return final