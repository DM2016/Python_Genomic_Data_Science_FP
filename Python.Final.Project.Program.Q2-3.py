#!/usr/bin/python
from Bio import SeqIO  #Import SeqIO from Bio
seq_lengths = "dna2.fasta" #define filename
for length in SeqIO.parse(seq_lengths, "fasta"):  #parse length of seq_lengths using SeqIO using for loop
        print("Sequence" + length.id + ", length " + str(len(length.seq))) #print results
