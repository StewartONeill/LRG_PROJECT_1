import xml.etree.ElementTree as ET
import csv
import argparse
import sys

		
def FileCheck(fn):
	try:
		open(fn, "r")
	except IOError:
		print("Error: File does not appear to exist")
		return "Error: File does not appear to exist."
		#sys.exit()
     
	 
	 
	 
	 #this is a test comment
	 

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

	bed_array = [['chromosome_number', 'exon_start', 'exon_end', 'exon_number']]

	symbol_element = root.find("./updatable_annotation/annotation_set[@type='ncbi']/features/gene/symbol")
	gene_name = symbol_element.get("name")
	mapping_element = root.find("updatable_annotation/annotation_set[@type='lrg']/mapping")
	chr_number = mapping_element.get("other_name")
	
	print("Gene Name is...", gene_name)

	for exon in root.findall("./fixed_annotation/transcript[@name='t1']/exon"):
		coords = exon.find("coordinates")
		
		exon_number = (exon.get("label"))
		coords_start = (coords.get("start"))
		coords_end = (coords.get("end"))
		
		list = [chr_number, coords_start, coords_end, exon_number ]
		for item in list:
			if item == "":
				print("Error: attribute empty")
				return 'Error: attribute empty'
				#sys.exit()
			elif item == None:
				print("Error: attribute missing")
				return 'Error: attribute missing'
				#sys.exit()
			else:
				pass
				
		bed_array.append(list)
	print(bed_array)
	
	filename = gene_name + ".bed"
	print("THE FILENAME IS..." + filename)

	with open(filename, 'w') as tsvFile:
		writer = csv.writer(tsvFile, delimiter='\t')
		writer.writerows(bed_array)
	tsvFile.close()
	return filename

if __name__ == '__main__':
	filepath = get_arguments()
	lrg2bed(filepath)