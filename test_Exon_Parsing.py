from Exon_Parsing import FileCheck, get_arguments, lrg2bed
import os
import pandas as pd
import argparse
import pytest

#tests if the correct gene name is derived when 'lrg_no=5' is used as input
def test_one():
	assert lrg2bed(outpath="./", lrg_no="5", filepath=None)[1]=="C1orf50"
