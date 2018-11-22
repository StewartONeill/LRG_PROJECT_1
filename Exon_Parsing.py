import xml.etree.ElementTree as ET
import csv

#Read in XML file.
file = "../LRG_XML/LRG_1.xml"
tree = ET.parse(file)
root = tree.getroot()
 
#Finds all exon elements within the fixed_annotation/transcript element. 
#Prints the exon attribute
#Prints the genomic start and end coords on this exon

bed_array = [['exon_number', 'exon_start', 'exon_end']]

lrg_id =root.find("./fixed_annotation/id").text
print("LRG_ID is...", lrg_id)

for exon in root.findall("./fixed_annotation/transcript/exon"):
	exon_number = (exon.get("label"))
	coords = exon.find("coordinates")
	coords_start = (coords.get("start"))
	coords_end = (coords.get("end"))
	list = [exon_number, coords_start, coords_end]
	bed_array.append(list)
print(bed_array)

filename = lrg_id + ".bed"
print(filename)

with open(filename, 'w') as tsvFile:
	writer = csv.writer(tsvFile, delimiter='\t')
	writer.writerows(bed_array)
tsvFile.close()