from .loader import load_quran
from .index import build_keys, build_texts
from .search import search

class AyahSearch:

    def __init__(self, quran, clean, simple):
        
        quran_root = load_quran(quran)
        clean_root = load_quran(clean)
        simple_root = load_quran(simple)

        self.keys = build_keys(quran_root)

        self.quran_text = build_texts(quran_root)
        self.clean_text = build_texts(clean_root)
        self.simple_text = build_texts(simple_root)

        self.suras = [sura.attrib["name"] for sura in quran_root.iter("sura")]

    def search(self, query):
        return search(
            query,
            self.keys,
            self.suras,
            self.quran_text,
            self.clean_text,
            self.simple_text
        )