#!/usr/bin/env python2
# Edited from SatoLab extract_vreads.py by NMS
# 2021.09.21
# This script extract reads assigned to features from blast_search
# Input: blast_result(output format 6)
# Output: query fasta file for previous blast
# 
import sys

blast_res = sys.argv[1]
fasta = sys.argv[2]

max_Eval = 1.0E-10

blast_f = open(blast_res, "r")
read_list = []
for line in blast_f:
    line = line.strip().split()
    read = line[0]
    Eval = line[10]
    Eval = float(Eval)

    if Eval < max_Eval:
        read_list.append(read)

read_set = set(read_list)

out = []
fst = open(fasta, "r")
fastl = []
for line in fst:
    line = line.strip()
    fastl.append(line)

for i in range(0,len(fastl),2):
    read = fastl[i]
    seq = fastl[i + 1]
    new_read = read.replace(">","")
    if new_read in read_set:
        l = [read,seq]
        print("\n".join(l))
