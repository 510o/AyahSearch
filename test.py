from searcher.segmenter import split_by_letters
from shutil import get_terminal_size
from main import plain_engine

RESHAPE = True  # set to False if you don't want to reshape the text for display

if RESHAPE:
    from arabicdisplayer import reshape, line_breaker, apply_display, align_text # pip install git+https://github.com/510o/ArabicDisplayer.git
    def formation(text: str, head: str = "", width: int = 0):
        if width:
            text = line_breaker(text, width)


        text = apply_display(text)

        if head and text.count('░') == len(head):
            head = iter(head)
            text = ''.join(
                next(head) if c == '░' else c
                for c in text
            )

        if width:
            text = align_text(text, width)

        return text


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
                chunks[i] = apply_display(reshape(chunk))

        print(formation(f"\n{'░' * len(repr(chunks))} {reshape("نتائج البحث")} {'░' * len(str(n))}░", f":{n}{chunks}", width))
    else:
        print(f"\n:نتائج البحث {n} {repr(chunks)}")

    for (sura, aya), text in verses.items():
        lverse = f"[{sura}: {aya}] "
        verse_len = len(lverse)

        if RESHAPE:
            print(formation('░' * verse_len + reshape(text), f" [{aya} :{sura}]", width))

        else:
            print(lverse + text)

    print("-" * width)