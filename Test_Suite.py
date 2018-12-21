from Exon_Parsing import lrg2bed 
import os
import pandas as pd

#filepath = "P:\Desktop\PROGRAMMING\LRG_XML"
#number_list = [os.path.join(filepath, f) for f in sorted(os.listdir(filepath))]
#print(xml_list)

for number in range(1, 9):
	number = str(number)
	file_output = lrg2bed(number)
	assert os.path.isfile(file_output), "Bed file not found for XML..." + xml
	df = pd.read_csv(file_output, sep='\t')
	length = len(df.index)
	print(length)
	print(df)
	