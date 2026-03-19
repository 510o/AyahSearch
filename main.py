from .searcher.engine import AyahSearch
from .config import BASE_DIR


plain_engine = AyahSearch(
    BASE_DIR / "Quran.xml",
    BASE_DIR / "clean.xml",
    BASE_DIR / "simple.xml"
)


uthmani_engine = AyahSearch(
    BASE_DIR / "Quran.xml",
    BASE_DIR / "uthmani-clean.xml",
    BASE_DIR / "uthmani-simple.xml"
)
