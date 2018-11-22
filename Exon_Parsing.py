import xml.etree.ElementTree as ET
import csv
import argparse
import sys

		
def FileCheck(fn):
	try:
		open(fn, "r")
	except IOError:
		print("Error: File does not appear to exist.")
		sys.exit()
     

def get_arguments():

	#Retrieve command line arguments
	parser = argparse.ArgumentParser()
	parser.add_argument("--file", help="path to xml file")
	args = parser.parse_args()
	filepath = args.file
	
	print(filepath)
	return filepath
	

def lrg2bed(lrg_xml):

	'''takes lrg.xml file as argument and outputs bedfile with exon_number, start and stop coordinates'''

	FileCheck(lrg_xml)
	
	#Read in XML file.
	file = lrg_xml
	tree = ET.parse(file)
	root = tree.getroot()
	 
	#Finds all exon elements within the fixed_annotation/transcript element. 
	#Prints the exon attribute
	#Prints the genomic start and end coords on this exon

	bed_array = [['exon_number', 'exon_start', 'exon_end']]

	lrg_id =root.find("./fixed_annotation/id").text
	print("LRG_ID is...", lrg_id)

	for exon in root.findall("./fixed_annotation/transcript[@name='t1']/exon"):
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

if __name__ == '__main__':
	filepath = get_arguments()
	lrg2bed(filepath)