from searcher.segmenter import split_by_letters
from shutil import get_terminal_size
from main import plain_engine

RESHAPE = True  # set to False if you don't want to reshape the text for display

if RESHAPE:
    from arabicreshaper import reshape # pip install git+https://github.com/510o/ArabicReshaper.git

print("Ayah Search - search by letter, diacritice, or numbers")

while True:
    query = input("search for: ")

    chunks = split_by_letters(query, plain_engine.letters)
    if len(chunks) == 1 and chunks[0] in ("exit", "stop", "quit", "break"):
        break

    results = plain_engine.search(query)

    verses = results.get("verses", {})
    n = len(verses)

    if RESHAPE:
        for i, chunk in enumerate(chunks):
            if chunk[0] in plain_engine.letters:
                chunks[i] = reshape(chunk)[::-1]

    print(f"\n{repr(chunks)} {n} results:")

    for (sura, aya), text in verses.items():
        print(f"[{sura}:{aya}] {reshape(text)[::-1] if RESHAPE else text}")

    print("-" * get_terminal_size().columns)