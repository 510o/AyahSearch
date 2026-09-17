from .diacritics import diac_rooms, combining
from .segmenter import split_by_letters
from re import finditer, sub


def verse_search(query, quran_index, clean_index, simple_index, suras, suras_found):
    query_rooms = diac_rooms(query)
    query_plain = "".join(c for c in query if not combining(c))
    with_diac = any(combining(c) for c in query)
    results = {}

    def matches(key):
        if not with_diac:
            return True
        simple_rooms = diac_rooms(f" {simple_index[key]} ")
        j = 0
        for l in simple_rooms:
            if query_rooms[j] in l:
                j += 1
                if j == len(query_rooms):
                    return True
            elif combining(l[0]) and not combining(query_rooms[j][0]):
                continue
            else:
                j = 0
        return False

    for key, text in clean_index.items():
        if suras_found and suras[key[0]] not in suras_found:
            continue
        if query_plain in f" {text} " and matches(key):
            results[key] = quran_index[key]

    return results


def number_search(nums, quran_index):
    if not nums:
        return {}

    sura, *rest = nums
    if rest and (key := (sura, rest[0])) in quran_index:
        return {key: quran_index[key]}

    if (key := (sura, 1)) in quran_index:
        return {key: quran_index[key]}

    return {}


def search(query, quran_index, clean_index, simple_index, suras, letters):
    if not query.strip():
        return {}

    num_matches = list(finditer(r"\d+", query))
    nums = [int(m.group()) for m in num_matches]

    suras_found = set()
    for sura in suras.values():
        if f"سورة {sura}" in query:
            suras_found.add(sura)
            query = sub(rf"و?سورة {sura}", "", query)

    chunks = split_by_letters(query, letters)
    text_chunk = ""

    for chunk in chunks:
        if chunk[0] in letters:
            text_chunk = chunk
            break

    if text_chunk:
        text_results = verse_search(text_chunk, quran_index, clean_index, simple_index, suras, suras_found)

        if nums:
            nums_set = set(nums)
            return {k for mapping in text_results.values() for k in mapping
                            if k[0 if chunks[0][0].isdigit() else 1] in nums_set}

        return text_results

    elif nums:
        return number_search(nums, quran_index)

    return {}