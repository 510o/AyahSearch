from searcher.segmenter import split_by_letters
from shutil import get_terminal_size
from main import plain_engine

RESHAPE = True  # set to False if you don't want to reshape the text for display

if RESHAPE:
    from arabicdisplayer import reshape, line_breaker, apply_display, align_text # pip install git+https://github.com/510o/ArabicDisplayer.git

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
                chunks[i] = reshape(chunk)

        head = f"\n{chunks} نتائج البحث {n}:"
        print(align_text(apply_display(line_breaker(reshape(head), width)), width))
        
    else:
        print(head)

    for (sura, aya), text in verses.items():
        verse = f"[{sura}: {aya}] {text}"
        if RESHAPE:
            print(align_text(apply_display(line_breaker(reshape(verse), width)), width))

        else:
            print(verse)

    print("-" * width)