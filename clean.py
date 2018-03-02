import re
import json

#Removing html tags and other special characters from the question.
def clean_text(raw_text):
    clean_html = re.compile('<.*?>')
    cleaned_html = re.sub(clean_html, '', raw_text)
    cleaned_html = re.sub('\\\\n', '', cleaned_html)
    cleaned_html = re.sub('\\\\t', '', cleaned_html)
    cleantext = re.sub(r'\W+',' ', cleaned_html)
    cleantext = re.sub('nbsp', '', cleantext)
    return cleantext

data = json.load(open("data.json"))

out = "Questions, Tags\n" #Header for output file
for tag in data:
    print("Working on " + tag + "...")
    temp = data[tag]
    for i in temp:
        question = clean_text(i)
        out = out + question + "," + tag + "\n"

with open("cleaned_dataset.csv", "w", encoding = "utf-8") as f:
    f.write(out)
print("Done :)")
