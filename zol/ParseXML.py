# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET

tree = ET.parse('folder/canon.xml')
root = tree.getroot()

for child in root:
    for children in child:
        print(child.tag, ":", children.text)
        break

