import bibtexparser
import os
from operator import itemgetter as i
from functools import cmp_to_key
workdir = "/mnt/6ba1dfab-4321-4db6-a970-de35184a6baa/ruslit/bibs/"


def cmp(x, y):
    return (x > y) - (x < y)


def multikeysort(items, columns):
    comparers = [
        ((i(col[1:].strip()), -1) if col.startswith('-')
         else (i(col.strip()), 1))
        for col in columns
    ]

    def comparer(left, right):
        comparer_iter = (
            cmp(fn(left), fn(right)) * mult
            for fn, mult in comparers
        )
        return next((result for result in comparer_iter if result), 0)
    return sorted(items, key=cmp_to_key(comparer))


with open(workdir + os.listdir(workdir)[0]) as bibtex_file:
    bib_database = bibtexparser.load(bibtex_file)

for bib in os.listdir(workdir)[1:]:
    with open(workdir + bib) as bibtex_file:
        bib_database.entries.extend(bibtexparser.load(bibtex_file).entries)

with open('consolidated.bib', 'w') as outfile:
    bibtexparser.dump(bib_database, outfile)

print(bib_database.entries[0])

a = multikeysort(bib_database.entries, ['volume', 'year'])

for entry in a:
    try:
        len(entry['abstract'])
    except Exception:
        print(entry['volume'], entry['year'])
