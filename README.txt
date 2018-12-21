---------------------------
- LRG to BED Parsing Tool -
---------------------------

Contributers: Ashley Pritchard, Stewart O’Neil and Helen Warren
README Created: 20-12-2018


DESCRIPTION

This tool enables the parsing of LRG (Locus Reference Genome) records into BED files. LRG is a fixed DNA sequence format that is independent of the genome. LRG was created to provide a stable framework for referencing genomic variants. The BED file format is a flexible and concise means to represent genomic coordinates. It is also a compatible file format for use with many genomic analysis tools. The BED file format supports 12 columns but only the first 3 are required: (1) chrom – the name of the chromosome and (2 and 3) start and end – the zero-based start position and one-based end position in the chromosome i.e. start=50, end=100 would span bases 51-100 inclusive. The tool outputs a BED file with the three required columns plus an additional exon number column. 

INSTALLATION

This tool requires Python (tested on version 2.7 and 3.5). Python can be downloaded here: https://www.python.org/downloads/
It is also necessary to install the wget Python module using pip. 

USER GUIDE

The tool must be provided with an LRG xml file. There are two options, both executable from the terminal:

1) python LRG_Exon_Parser.py --file FILEPATH
2) python LRG_Exon_Parser.py --lrg_no X

Option 1 should be employed when the LRG .xml file is stored locally. ‘FILEPATH’ should be replaced with the filepath of the LRG record. 

Option 2 offers more flexibility. ‘X’ should be replaced with the respective LRG ID number. The tool will first check whether the LRG .xml file is present locally. If not, the tool will retrieve the LRG .xml file  from the online LRG database, save it in the current directory and commence parsing. 

The output is the same for both options. The gene name and resultant BED file are printed to terminal. The BED file is also saved in the current directory as ‘gene name’.bed. 

SUPPORT

If you need support when using this tool, please email one of the following contributers:
ashley.pritchard@postgrad.manchester.ac.uk
stewart.oneill@postgrad.manchester.ac.uk
helen.warren@postgrad.manchester.ac.uk


CONTRIBUTIONS

Contributions to the project can be made via GitHub by cloning the following repository: https://github.com/StewartONeill/LRG_PROJECT_1.git

ROADMAP 

The next version of this tool will include the capability of converting from LRG coordinates to GRCh37 or GRCh38 coordinates.
