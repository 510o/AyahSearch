from .diacritics import diac_rooms, combining
import re

def split_by_letters(query, letters, space = " "):
    parts, current = [], []
    neutral, check = 0, None

    for chr in query:
        if chr == space:
            neutral += 1
            continue

        in_letters = chr in letters

        if check is None:
            if in_letters and neutral:
                current.append(space)

            current.append(chr)

        elif in_letters == check:
            if neutral:
                current.append(space)

            current.append(chr)

        elif neutral > 1:
            if check:
                current.append(space)
                parts.append("".join(current))
                current = [chr]

            else:
                parts.append("".join(current))
                current = [space, chr]

        else:
            parts.append("".join(current))
            current = [chr]

        check = in_letters
        neutral = 0

    if neutral and check:
        current.append(space)

    if current:
        parts.append("".join(current))

    return parts


def verse_search(query, quran_index, clean_index, simple_index, suras):
    query_rooms = diac_rooms(query)
    query_plain = "".join(c for c in query if not combining(c))
    with_diac = any(combining(c) for c in query)
    results = {}

    for key, text in clean_index.items():
        if key[1] == 1 and query in suras[key[0]]:
            results.setdefault("suras", {})[key] = quran_index[key]

        if query_plain in f" {text} ":
            if with_diac:
                simple_rooms = diac_rooms(f" {simple_index[key]} ")
                j = 0
                for l in simple_rooms:
                    if query_rooms[j] in l:
                        j += 1
                        if j == len(query_rooms):
                            results.setdefault("verses", {})[key] = quran_index[key]
                            break
                    elif combining(l[0]) and not combining(query_rooms[j][0]):
                        continue
                    else:
                        j = 0
            else:
                results.setdefault("verses", {})[key] = quran_index[key]

    return results


def number_search(nums, quran_index):
    if not nums:
        return {}

    sura = nums[0]

    print(nums)  
    if len(nums) > 1:
        aya = nums[1]
        key = (sura, aya)
        if key in quran_index:
            return {"verses": {key: quran_index[key]}}

    key = (sura, 1)
    if key in quran_index:
        return {"suras": {key: quran_index[key]}}

    return {}


def search(query, quran_index, clean_index, simple_index, suras, letters):
    chunks = split_by_letters(query, letters)

    if not chunks:
        return {}

    text_chunk = ""
    nums = []

    for chunk in chunks[:2]:
        if chunk.strip()[0] in letters:
            text_chunk = chunk
        else:
            nums = [int(m.group()) for m in re.finditer(r"\d+", chunk)]

    if text_chunk:
        if nums:
            text_results = verse_search(text_chunk, quran_index, clean_index, simple_index, suras)

            filtered = {}
            for key_type, mapping in text_results.items():
                filtered[key_type] = {k: v for k, v in mapping.items() if k[1] in nums}
            return filtered

        else:
            return verse_search(text_chunk, quran_index, clean_index, simple_index, suras)

    elif nums:
        return number_search(nums, quran_index)
    
    return {}