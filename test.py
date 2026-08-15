from searcher.segmenter import split_by_letters
from shutil import get_terminal_size
from main import plain_engine

RESHAPE = True  # set to False if you don't want to reshape the text for display

if RESHAPE:
    from arabicdisplayer import reshape, line_breaker, apply_display, align_text # pip install git+https://github.com/510o/ArabicDisplayer.git
    from unicodedata import combining
    def build_header(body, prefix="", suffix="", width=0, right_alignment=False):
        vlen = lambda line: sum(not combining(c) for c in line)

        body = reshape(body)
        if width:
            offset = min(vlen(prefix), width)
            body = line_breaker(body, width, first_line_offset=offset)
        lines = apply_display(body).split('\n')

        lines[-1] = lines[-1] + prefix
        lines[0] = suffix + lines[0]

        return align_text('\n'.join(lines), width, right_alignment) if width else '\n'.join(lines)

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

        head = f"{chunks} نتائج البحث {n}:"
        
        print(build_header("نتائج البحث", f" {chunks}", f":{n} ", width, True))
        
    else:
        print(head)

    for (sura, aya), text in verses.items():
        if RESHAPE:
            head = f" [{aya} :{sura}]"
            print(build_header(text, head, "", width, True))

        else:
            print(f"[{sura}: {aya}] {text}")

    print("-" * width)