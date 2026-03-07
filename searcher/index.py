def build_keys(root):
    return [
        (int(sura.attrib["index"]), int(aya.attrib["index"]))
        for sura in root.iter("sura")
        for aya in sura.iter("aya")
    ]

def build_texts(root):
    return [
        aya.attrib["text"]
        for sura in root.iter("sura")
        for aya in sura.iter("aya")
    ]