import xml.etree.ElementTree as ET
import csv
import argparse
import wget
import pandas as pd

def FileCheck(fn):
	'''Check whether the file exists'''
	try:
		open(fn, "r")
	except OSError :
		print("\nNOTE: File", fn, "does not appear to exist")
		return OSError


def get_arguments():

	'''Parse command line arguments'''

	parser = argparse.ArgumentParser()
	parser.add_argument("--outpath", help="outpath for BED file", default="")
	group = parser.add_mutually_exclusive_group(required=True)
	group.add_argument("--lrg_no", help="LRG number")
	group.add_argument("--file", help="path to xml file")
	args = parser.parse_args()
	return args

def lrg2bed(outpath, lrg_no=None, filepath=None):

	'''
	Take an lrg number or a filepath and output bedfile. 
	The output BED file has the following columns: chromosome number, 
	exon_number, start and stop coordinates.
	'''

	# If an lrg no. has been given, checks whether the file exists locally.
	# Downloads the file if no local copy is found.
	if lrg_no != None and filepath == None:
		file_name = "LRG_" + str(lrg_no) + ".xml"
		if FileCheck(file_name) is OSError:
			print("\nAttempting to download", file_name, "from url...")
			url = "http://ftp.ebi.ac.uk/pub/databases/lrgex/" + file_name
			print(url)
			try:
				file = wget.download(url)
				print("\nSuccessfully downloaded...", file)
			except:
				print("\nHTTPError: URL does not exist.")
				return
	
	'''
	If the XML file already exists locally, 
	a print statement will convey this to the terminal 
	and the local XML file will be used to create the BED file.
	'''
		elif FileCheck(file_name) is None:
			print("An existing local XML file has been found for this LRG no." 
				  "\nThis local file will be used to generate the BED file")
			file = file_name

	# If a filepath has been given, checks whether the file exists 
	if filepath != None and lrg_no == None:				
		if FileCheck(filepath) is OSError:
			return
		else:
			file = filepath

	# Checks that only one of the two possible arguments has been provided
	if filepath != None and lrg_no != None:
		msg = 'Please provide either a filepath or an lrg number, not both.'
		print(msg)
		return msg

	#Read in XML file
	tree = ET.parse(file)
	root = tree.getroot()
	
	print("Converting XML file to BED file.\n")
	
	#Create an array for the eventual BED file, with headings for each column.
	bed_array = [['chromosome_number', 'exon_start', 'exon_end', 'exon_number']]
	
	#Select and print the gene name from the XML file.
	symbol_element = root.find("./updatable_annotation/annotation_set"
							   "[@type='ncbi']/features/gene/symbol")
	gene_name = symbol_element.get("name")
	print("Gene Name is...", gene_name)
	
	#Select the chromosome number of the gene.
	mapping_element = root.find("updatable_annotation/annotation_set"
								"[@type='lrg']/mapping")
	chr_number = mapping_element.get("other_name")
	
	
	'''
	Finds all exon elements within the fixed_annotation/transcript element.
	Stores the chromosome number, the exon number and the start and end coordinates
	of the exon into a list. If any item in this list is empty or missing, print an error message.
	'''
	for exon in root.findall("./fixed_annotation/transcript[@name='t1']/exon"):
		coords = exon.find("coordinates")
		exon_number = (exon.get("label"))
		coords_start = (coords.get("start"))
		coords_end = (coords.get("end"))
		list = [chr_number, coords_start, coords_end, exon_number ]
		for item in list:
			if item == "":
				print("\nError: attribute empty")
				return 'Error: attribute empty'
			elif item == None:
				print("\nError: attribute missing")
				return 'Error: attribute missing'
			else:
				pass
		bed_array.append(list)

	filename = gene_name + ".bed"
	filepath = outpath + filename
	print("\nTHE FILENAME IS..." + filename)

	#Save the BED file in TSV format
	with open(filepath, 'w') as tsvFile:
		writer = csv.writer(tsvFile, delimiter='\t')
		writer.writerows(bed_array)
	tsvFile.close()
	print("\n-------File " + filename + " has been created-------")

	#Load the BED file into pandas df and print to terminal
	df = pd.read_csv(filepath, sep='\t')
	print(df.to_string(index=False))

	return(filename, gene_name)


if __name__ == '__main__':

	print("\nRetrieving arguments...\n")
	args = get_arguments()
	print("LRG Number =", args.lrg_no)
	print("Filepath =", args.file, "\n")

	if args.lrg_no != None:
		lrg2bed(outpath=args.outpath, lrg_no=args.lrg_no)
	if args.file != None:
		lrg2bed(outpath=args.outpath, filepath=args.file)

