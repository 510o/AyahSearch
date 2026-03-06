from searcher.engine import AyahSearch
from config import BASE_DIR

engine = AyahSearch(
    BASE_DIR / "Quran.xml",
    BASE_DIR / "quran-clean.xml",
    BASE_DIR / "quran-simple.xml"
)

results = engine.search("كسْفا")

for (sura, aya), text in results:
    print(sura, aya, text)