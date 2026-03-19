def build_index(root):
    return {
        (int(sura.attrib["index"]), int(aya.attrib["index"])): aya.attrib["text"]
        for sura in root.iter("sura")
        for aya in sura.iter("aya")
    }

def build_data(root):
    index = {}
    sura_names = {}
    letters = set()

    for sura in root.iter("sura"):
        sura_names[int(sura.attrib["index"])] = sura.attrib["name"]

        for aya in sura.iter("aya"):
            index[(int(sura.attrib["index"]), int(aya.attrib["index"]))] = aya.attrib["text"]

            for ch in aya.attrib["text"]:
                letters.add(ch)

    return index, sura_names, letters