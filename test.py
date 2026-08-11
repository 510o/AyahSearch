from searcher.segmenter import split_by_letters
from shutil import get_terminal_size
from main import plain_engine

RESHAPE = True  # set to False if you don't want to reshape the text for display

if RESHAPE:
    from arabicreshaper import reshape, line_breaker # pip install git+https://github.com/510o/ArabicReshaper.git

print(line_breaker("Ayah Search - search by letters, diacritices, or numbers", get_terminal_size().columns))

while True:
    query = input("search for: ")
    width = get_terminal_size().columns

    chunks = split_by_letters(query, plain_engine.letters)
    if len(chunks) == 1 and chunks[0] in ("exit", "stop", "quit", "break"):
        break

    results = plain_engine.search(query)

    verses = results.get("verses", {})
    n = len(verses)

    if RESHAPE:
        for i, chunk in enumerate(chunks):
            if chunk[0] in plain_engine.letters:
                chunks[i] = reshape(chunk, True)

    print(f"\n{repr(chunks)} {n} results:")

    for (sura, aya), text in verses.items():
        head = f"[{sura}: {aya}] "
        head_len = len(head)
        print(f"{head}{reshape(line_breaker("░"*head_len + text, width).replace("░", "", head_len), True) if RESHAPE else text}")

    print("-" * width)