from Exon_Parsing import lrg2bed 
import os

filepath = "P:\Desktop\PROGRAMMING\LRG_XML"
xml_list = [os.path.join(filepath, f) for f in sorted(os.listdir(filepath))]
#print(xml_list)

for xml in xml_list:
	file_name = lrg2bed(xml)
	assert os.path.isfile(file_name), "Bed file not found for XML..." + xml
	