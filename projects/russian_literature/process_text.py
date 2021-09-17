import os
import fitz
import string
import json
import tqdm
import bibtexparser
from guess_language import guess_language
from nltk.corpus import stopwords
import nltk
workdir = "/mnt/6ba1dfab-4321-4db6-a970-de35184a6baa/ruslit/pdfs/"

result = {}
nltk.download('stopwords')

stop_words = set(stopwords.words('english'))

with open('consolidated.bib') as bibtex_file:
    bib_database = bibtexparser.load(bibtex_file)

not_english = 0

for pdf in tqdm.tqdm(os.listdir(workdir)):
    with fitz.open(workdir + pdf) as doc:
        text = ""
        for page in doc:
            text += page.getText().strip()
        # guess language
        if guess_language(text) != 'en':
            not_english += 1
            continue
        # convert text to list of words
        text = text.translate(str.maketrans('', '', string.punctuation))
        text = text.replace('\t', "")
        text = text.replace('\n', "")
        text = text.lower()
        text = text.split()
        text = [w for w in text if not w.lower() in stop_words]
        result[pdf] = text

print("")
print("Not english, sorted out:", not_english)

with open('ruslit_raw.json', 'w') as f:
    json.dump(result, f)
