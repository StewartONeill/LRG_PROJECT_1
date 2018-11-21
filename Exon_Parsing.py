import xml.etree.ElementTree as ET


#Read in XML file.
file = "../LRG_XML/LRG_1.xml"
tree = ET.parse(file)
root = tree.getroot()
 
#Finds all exon elements within the fixed_annotation/transcript element. 
#Prints the exon tag and attribute
for exon in root.findall("./fixed_annotation/transcript/exon"):
#
#/[@coord_system='LRG_1']"):
	print(exon.tag, exon.attrib)

	 
