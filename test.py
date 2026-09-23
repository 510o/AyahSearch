from subprocess import Popen
from os import system, name
import sys

from searcher.segmenter import split_by_letters
from shutil import get_terminal_size
from main import plain_engine

if RESHAPE := True: # set to False if you don't want to reshape the text for display
    from arabicdisplayer import reshape, line_breaker, apply_display, align_text # pip install git+https://github.com/510o/ArabicDisplayer.git

print(line_breaker("Ayah Search - search by letters, diacritices, or numbers", get_terminal_size().columns))
clear = lambda: system('cls' if name == 'nt' else 'clear')

while True:
    query = input("search for: ")

    width = get_terminal_size().columns
    chunks = split_by_letters(query, plain_engine.letters)

    if len(chunks) == 1:
        if chunks[0] in ("exit", "stop", "quit", "break"):
            break

        elif chunks[0] == "reset":
            print()
            process = Popen([sys.executable] + sys.argv)
            process.wait()
            sys.exit(process.returncode)

        elif chunks[0] == "clear":
            clear()
            continue

    results = plain_engine.search(query)
    n = len(results)
    head = f"\n{chunks} نتائج البحث {n}:"

    if RESHAPE:
        input_layout = apply_display(line_breaker(reshape(f"search for: {query}"), width))
        for _ in range(input_layout.count("\n") +1):
            sys.stdout.write("\033[F\033[K")
        sys.stdout.flush()
        print(input_layout)

        for i, chunk in enumerate(chunks):
            if chunk[0] in plain_engine.letters:
                chunks[i] = reshape(chunk)

        print(align_text(apply_display(line_breaker(reshape(head), width)), width))
        
    else:
        print(head)

    if n:
        for (sura, aya), text in results.items():
            verse = f"{plain_engine.suras[sura]} [{sura}: {aya}] {text}"
            if RESHAPE:
                print(align_text(apply_display(line_breaker(reshape(verse), width)), width))

            else:
                print(verse)

    print("-" * width)