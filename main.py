from searcher.engine import AyahSearch
from config import BASE_DIR

plain_engine = AyahSearch(
    BASE_DIR / "Quran.xml",
    BASE_DIR / "clean.xml",
    BASE_DIR / "simple.xml"
)

#results = plain_engine.search("كسْفا")

#for (sura, aya), text in results:
#    print(sura, aya, text)


uthmani_engine = AyahSearch(
    BASE_DIR / "Quran.xml",
    BASE_DIR / "uthmani-clean.xml",
    BASE_DIR / "uthmani-simple.xml"
)

results = uthmani_engine.search("")

for (sura, aya), text in results:
    print(sura, aya, text)