from searcher.engine import AyahSearch
from config import BASE_DIR


plain_engine = AyahSearch(
    BASE_DIR / "Quran.xml",
    BASE_DIR / "clean.xml",
    BASE_DIR / "simple.xml"
)

word = plain_engine.search("كسْفا")
num = plain_engine.search("")
sura = plain_engine.search("إسراء")

for result in num:
    print(*result) 


uthmani_engine = AyahSearch(
    BASE_DIR / "Quran.xml",
    BASE_DIR / "uthmani-clean.xml",
    BASE_DIR / "uthmani-simple.xml"
)

results = uthmani_engine.search("ناكسوا")

#for (sura, aya), text in results:
#    print(sura, aya, text)