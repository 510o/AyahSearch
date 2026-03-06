from unicodedata import combining

def diac_rooms(text):
    result = []
    for sym in text:
        if not result:
            result.append(sym)
            continue

        if combining(sym) and combining(result[-1][0]):
            result[-1] += sym
        else:
            result.append(sym)

    return result