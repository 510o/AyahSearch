from xml.etree.ElementTree import parse
from unicodedata import combining
from config import BASE_DIR

INPUT_FILE = BASE_DIR / "uthmani-min.xml"
OUTPUT_FILE = BASE_DIR / "uthmani-clean.xml"


def clean_quran():
    tree = parse(INPUT_FILE)
    root = tree.getroot()

    for aya in root.iter("aya"):
        if "text" in aya.attrib:
            aya.attrib["text"] = "".join(c for c in aya.attrib["text"] if not combining(c))

        if "bismillah" in aya.attrib:
            aya.attrib["bismillah"] = "بسم الله الرحمن الرحيم"

    tree.write(OUTPUT_FILE, encoding="utf-8", xml_declaration=True)


if __name__ == "__main__":
    clean_quran()