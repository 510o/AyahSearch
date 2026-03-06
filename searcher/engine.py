from .loader import load_quran
from .index import build_index
from .search import search

class AyahSearch:

    def __init__(self, quran, clean, simple):

        self.quran_index = build_index(load_quran(quran))
        self.clean_index = build_index(load_quran(clean))
        self.simple_index = build_index(load_quran(simple))

    def search(self, query):
        return search(
            query,
            self.quran_index,
            self.clean_index,
            self.simple_index
        )