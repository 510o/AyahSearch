from .diacritics import diac_rooms, combining
from re import findall


def number_search(nums, keys, quran_text):
    sura = nums[0]
    
    if len(nums) > 1:
        aya = nums[1]
        return [
            (key, text)
            for key, text in zip(keys, quran_text)
            if key[0] == sura and key[1] == aya
        ]

    return [
        (key, text)
        for key, text in zip(keys, quran_text)
        if key[0] == sura and key[1] == 1
    ]


def sura_search(query, key, suras):
    return key[1] == 1 and query in suras[key[0] -1]


def search(query: str, keys, suras, quran_text, clean_text, simple_text):
    if not query.strip():
        return []
    
    if nums := list(map(int, findall(r"\d+", query))): 
        return number_search(nums, keys, quran_text)

    query_rooms = diac_rooms(query)
    query_plain = "".join(c for c in query if not combining(c))
    with_diac = any(combining(c) for c in query)
    results = []

    for i, text in enumerate(clean_text):
        if sura_search(query_plain, keys[i], suras):
            results.append((keys[i], quran_text[i]))

        elif query_plain in text:
            if with_diac:
                simple_rooms = diac_rooms(simple_text[i])
                j = 0

                for l in simple_rooms:
                    if query_rooms[j] in l:
                        j += 1
                        if j == len(query_rooms):
                            results.append((keys[i], quran_text[i]))
                            break

                    elif combining(l[0]) and not combining(query_rooms[j][0]):
                        continue

                    else:
                        j = 0
                        
            else:
                results.append((keys[i], quran_text[i]))
    return results