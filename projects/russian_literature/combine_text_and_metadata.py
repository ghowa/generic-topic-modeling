import json
import bibtexparser
from fuzzywuzzy import fuzz
import tqdm

with open("ruslit_raw.json") as f:
    documents = json.load(f)

with open("consolidated.bib") as bibtex_file:
    bib_db = bibtexparser.load(bibtex_file)

output_json = []

not_found = []

for doc in tqdm.tqdm(documents):
    year = doc.split("_")[1]
    most_likely = []
    max_ratio = 0
    for entry in bib_db.entries:
        ratio = 0
        try:
            # problems with long titles, footnotes in titles
            ratio = fuzz.ratio(doc.split("_")[0], entry['title'])
        except KeyError:
            continue
        if ratio > max_ratio:
            max_ratio = ratio
            most_likely = entry

    if(most_likely['year'] != year):
        not_found.append(doc)
    else:
        entry = {}
        num = "0"
        author = ""
        try:
            num = most_likely["number"]
        except KeyError:
            print("No number for ", most_likely['title'])
        try:
            author = most_likely["author"]
        except KeyError:
            print("No author for ", most_likely['title'])
        title = most_likely['title']
        entry["title"] = title
        entry["url"] = doc
        entry["date"] = most_likely["year"]
        entry["author"] = author
        entry["pages"] = most_likely["pages"]
        entry["volume"] = most_likely["volume"]
        entry["issue"] = num
        entry["text"] = documents[doc]
        output_json.append(entry)

# remove texts without metadata
for key in not_found:
    documents.pop(key, None)

with open("russian_literature.json", "w") as outfile:
    json.dump(output_json, outfile)
