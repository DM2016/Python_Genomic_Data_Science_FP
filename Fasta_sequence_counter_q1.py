#!/usr/bin/python
import Bio
from Bio import SeqIO
with open('dna.example.fasta', 'r') as f:  #open the dna exmaple fasta file to read, change file names accordingly wherever they occur
        seq_count = 0
        for seq in SeqIO.parse('dna.example.fasta', "fasta"):
                seq_count = seq_count + 1
        print("There were " + str(seq_count) + " records in file " + "dna.example.fasta")

f.close()
