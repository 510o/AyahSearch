import xml.etree.ElementTree as ET

def load_quran(path):
    return ET.parse(path).getroot()