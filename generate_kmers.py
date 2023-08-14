#!/usr/bin/env python
import argparse

def read_fasta(filename):
    sequences = []
    with open(filename, "r") as file:
        seq = ""
        for line in file:
            line = line.strip()
            if line.startswith(">"):
                if seq:
                    sequences.append((name, seq))
                name = line[1:]
                seq = ""
            else:
                seq += line
        if seq:
            sequences.append((name, seq))
    return sequences

def generate_kmer(name, sequence, k):
    kmer_list = []
    for i in range(len(sequence) - k + 1):
        kmer_list.append(f">{name}__{i+1}\n{sequence[i:i+k]}")
    return kmer_list

# 参数解析
parser = argparse.ArgumentParser(description="Generate kmer sequences from FASTA file")
parser.add_argument("-i", "--input", help="input FASTA file")
parser.add_argument("-k", "--kmer", type=int, default=150, help="kmer length (default: 150)")
args = parser.parse_args()

if not args.input:
    parser.print_help()
    exit()

input_file = args.input
output_file = "split_150bp.fa"
k = args.kmer

sequences = read_fasta(input_file)
with open(output_file, "w") as file:
    for name, sequence in sequences:
        kmers = generate_kmer(name, sequence, k)
        for kmer in kmers:
            file.write(kmer + "\n")
        file.write("\n")

print("Kmer sequences have been generated and saved to", output_file)
