# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
from xml.dom import minidom


def subElement(root, tag, text):
    ele = ET.SubElement(root, tag)
    ele.text = text


def saveXML(root, filename, indent="  ", newl="\n", encoding="gbk"):
    rawText = ET.tostring(root)
    dom = minidom.parseString(rawText)
    with open(filename, 'w') as f:
        dom.writexml(f, "", indent, newl, encoding)


root = ET.Element('note')
# to = root.makeelement("to", {})
# to.text = "peter"
# to.tail = '\n'
# root.append(to)

subElement(root, "来自".encode('utf-8').decode('utf-8'), "kevin")
subElement(root, "标题", "Reminder")
subElement(root, "内容", "dunno forget the meeting!")

tree = ET.ElementTree(root)
tree.write("note1.xml", encoding='utf-8', xml_declaration=True)
# saveXML(root, "note1.xml")

