from unicodedata import combining
import xml.etree.ElementTree as ET
from config import BASE_DIR

def build_index(root):
    return {
        (sura.attrib["name"], int(aya.attrib["index"])): aya.attrib["text"]
        for sura in root.iter("sura")
        for aya in sura.iter("aya")
    }

quran_index = build_index(ET.parse(BASE_DIR / "Quran.xml").getroot())
clean_index = build_index(ET.parse(BASE_DIR / "quran-clean.xml").getroot())
simple_index = build_index(ET.parse(BASE_DIR / "quran-simple.xml").getroot())
# uthmani_index = build_index(ET.parse(BASE_DIR / "quran-uthmani.xml").getroot())

def diac_rooms(text):
    result = []
    for sym in text:
        if not result: result.append(sym); continue
        if combining(sym) and combining(result[-1][0]): result[-1] += sym
        else: result.append(sym)
    return result

def search(query):
    query_plain = "".join(c for c in query if not combining(c))
    has_diac = any(combining(c) for c in query)
    results = []

    for key, clean_text in clean_index.items():
        if query_plain in clean_text:
            if has_diac:
                i, simple_rooms, query_rooms = 0, diac_rooms(simple_index[key]), diac_rooms(query)
                for l in simple_rooms:
                    if query_rooms[i] in l:
                        i += 1
                        if i == len(query_rooms): results.append((key, quran_index[key])); break
                    elif combining(l[0]) and not combining(query_rooms[i]): continue
                    else: i = 0
            else:
                results.append((key, quran_index[key]))
                
    return results