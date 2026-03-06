from xml.etree.ElementTree import parse
from unicodedata import combining
from config import BASE_DIR

uthmani = BASE_DIR / "uthmani.xml"
clean = BASE_DIR / "uthmani-clean.xml"
simple = BASE_DIR / "uthmani-simple.xml"

def simple_uthmani():
    tree = parse(uthmani)
    root = tree.getroot()

    for aya in root.iter("aya"):
        if "text" in aya.attrib:
            aya.attrib["text"] = "".join(c for c in aya.attrib["text"] if c not in "ـۦۥ")

    tree.write(simple, encoding="utf-8", xml_declaration=True)

def clean_uthmani():
    tree = parse(simple)
    root = tree.getroot()

    for aya in root.iter("aya"):
        if "text" in aya.attrib:
            aya.attrib["text"] = "".join(c for c in aya.attrib["text"] if not combining(c))

        if "bismillah" in aya.attrib:
            aya.attrib["bismillah"] = "بسم الله الرحمن الرحيم"

    tree.write(clean, encoding="utf-8", xml_declaration=True)


if __name__ == "__main__":
    simple_uthmani()
    clean_uthmani()