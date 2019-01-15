from Exon_Parsing import FileCheck, get_arguments, lrg2bed
import os
import pandas as pd
import argparse
import pytest

# tests if giving incorrect filename to FileCheck results in OSError
def test_notafile():
	assert FileCheck('thisisnotafile') == OSError

# tests if giving both lrg_no and filepath to lrg2bed generates expected error
def test_input():
	msg = 'Please provide either a filepath or an lrg number, not both.'
	assert lrg2bed(lrg_no=True, filepath=True, outpath=True) == msg

#tests if the correct gene name is derived when 'lrg_no=5' is used as input
def test_genename():
        assert lrg2bed(outpath="./", lrg_no="5", filepath=None)[1]=="C1orf50"
    
# creates instance of lrg2bed output to use in subsequent tests	
@pytest.fixture
def test_file():
	try:
		os.mkdir('test')
	except:
		FileExistsError
	lrg2bed(lrg_no='28', outpath="test/")
	return pd.read_csv("test/C5.bed", sep='\t')

# tests whether BED file is created
def test_save(test_file):
	assert os.path.isfile("test/C5.bed")

# tests whether BED file has the correct headers
def test_columns(test_file):
	cols = ['chromosome_number', 'exon_start', 'exon_end', 'exon_number']
	assert list(test_file.columns.values) == cols

# tests whether BED file contains correct datatype 
def test_dtype(test_file):
	for column in list(test_file.columns.values):
		assert test_file[column].dtype == int

# tests whether BED file outputs the correct chromosome number 
def test_chr(test_file):
	assert test_file.iloc[0,0] == 9

#tests whether BED file outputs the correct exon start and end location for exon number 1
def test_exon(test_file):
	assert test_file.iloc[0,1] == 5001 and test_file.iloc[0,2] == 5095

	



     

