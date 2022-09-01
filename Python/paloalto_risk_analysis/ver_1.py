import xml.etree.ElementTree as ET

xml_file = 'D:\\02_Programming\\Python\\paloalto_risk_analysis\\test.xml'
tree = ET.parse(xml_file)

user = tree.findall('./user/name/entry')
for i in user:
    print(i.text)

user = tree.findall('./user/name')
for i in user:
    print(i.text)