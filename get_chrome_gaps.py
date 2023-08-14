#!/usr/bin/env python
import argparse
import re
from Bio import SeqIO
# this code was changed based on biostar "https://www.biostars.org/p/152592/"
def count_chromosome_gaps(input_file, output_file):
    # Open input FASTA file, search for masked regions, print in GFF3 format
    with open(input_file) as handle:
        i = 0
        for record in SeqIO.parse(handle, "fasta"):
            for match in re.finditer('N+', str(record.seq)):
                i = i + 1
                output_file.write(record.id + "\t.\tgap\t" + str(match.start() + 1) + "\t" + str(match.end()) + "\t.\t.\t.\tName=gap" + str(i) + ";size=" + str(match.end() - match.start()) + "\n")

# Parse command-line arguments
parser = argparse.ArgumentParser(description='Count chromosome gaps in a FASTA file and save the result in GFF3 format.')
parser.add_argument("-i", "--input", required=True, help="Input FASTA file")
parser.add_argument("-o", "--output", required=True, help="Output GFF3 file")
args = parser.parse_args()

# Check if input and output file paths are provided
if args.input is None or args.output is None:
    parser.print_usage()
    exit()

# Open output GFF3 file
with open(args.output, 'w') as output:
    # Call count_chromosome_gaps() function to count gaps and write to output file
    count_chromosome_gaps(args.input, output)
