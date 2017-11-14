#!/usr/bin/python
import Bio
from Bio import SeqIO
with open('dna.example.fasta', 'r') as f:  #open the dna exmaple fasta file to read, change file names accordingly wherever they occur
        seq_count = 0 #set initial seq_count value at 0
        for seq in SeqIO.parse('dna.example.fasta', "fasta"): #use for loop to call SeqIO function parse on fasta file
                seq_count = seq_count + 1 #perform and keep track of seq_count
        print("There were " + str(seq_count) + " records in file " + "dna.example.fasta") #print results

f.close() #close program
