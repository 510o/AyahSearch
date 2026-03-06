from xml.etree.ElementTree import parse

def load_quran(path):
    return parse(path).getroot()