#!/usr/bin/python
# Corrinne Grover, September 2014

import sys
from cogent import LoadSeqs, DNA

if len(sys.argv) < 3:
    print "This program removes sequences from an mfasta file by EXACT sequence id."
    print "Usage: removeseqs_fromFasta input_file output_file.fasta seqid1 seqid2 ... seqidN"
    print "This program requires the output file to have the extension .fasta"
    print " "
    sys.exit()

cmdargs = sys.argv[3:]

aln = LoadSeqs(sys.argv[1], moltype=DNA, format='fasta')

removedseqs=aln.takeSeqs(cmdargs,negate=True)
removedseqs.toFasta()
removedseqs.writeToFile(sys.argv[2])

sys.exit()
