from unicodedata import combining

def diac_rooms(text):
    if not text.strip():
        return []
    
    result = [text[0]]
    for sym in text[1:]:
        if combining(sym) and combining(result[-1][0]):
            result[-1] += sym
        else:
            result.append(sym)

    return result