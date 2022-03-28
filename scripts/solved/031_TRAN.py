# https://rosalind.info/problems/tran/

file = "data/tran.txt"


def read_fasta(file: str):
    """
    Args
    file: path of fasta file
    """
    with open(file) as f:
        fa = f.read().splitlines()
    prev = True
    header = []
    seq = []
    for f in fa:
        if ">" in f:
            header.append(f[1:])
            prev = True
        elif prev:
            seq.append(f)
            prev = False
        else:
            seq[-1] += f
    return header, seq


_, seq = read_fasta(file)

seq1, seq2 = seq

transition = 0
transversion = 0

import re

for s1, s2 in zip(seq1, seq2):
    if s1 == s2:
        continue
    s = s1 + s2
    if re.match(r"(AG)|(GA)|(CT)|(TC)", s):
        transition += 1
    else:
        transversion += 1

print(transition / transversion)

