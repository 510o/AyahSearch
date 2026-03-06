def build_index(root):
    return {
        (sura.attrib["name"], int(aya.attrib["index"])): aya.attrib["text"]
        for sura in root.iter("sura")
        for aya in sura.iter("aya")
    }