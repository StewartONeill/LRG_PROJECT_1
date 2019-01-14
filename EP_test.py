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
	assert lrg2bed(lrg_no=True, filepath=True, outpath=True) == 'Please provide either a filepath or an lrg number, not both.'

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
	assert list(test_file.columns.values) == ['chromosome_number', 'exon_start', 'exon_end', 'exon_number']

# tests whether BED file contains correct datatype
def test_dtype(test_file):
	for column in list(test_file.columns.values):
		assert test_file[column].dtype == int

	

