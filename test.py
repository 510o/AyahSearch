from arabicreshaper import reshape # pip install git+https://github.com/510o/ArabicReshaper.git
from main import plain_engine

print("Ayah Search - search by letter, diacritice, or numbers")

while True:
    i = input("search for: ")
    if i in ("exit", "stop", "quit", "break"):
        break

    results = plain_engine.search(i)

    verses = results.get("verses", {})
    n = len(verses)

    print(f"\n{repr(reshape(i)[::-1])} {n} results:")

    for (sura, aya), text in verses.items():
        shaped = reshape(text)[::-1]
        print(f"[{sura}:{aya}] {shaped}")

    print("-" * 40)