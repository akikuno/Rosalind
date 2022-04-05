# https://rosalind.info/problems/pmch/


def fmtfa(fasta: list):
    prev = True
    header = []
    seq = []
    for f in fasta:
        if ">" in f:
            header.append(f[1:])
            prev = True
        elif prev:
            seq.append(f)
            prev = False
        else:
            seq[-1] += f
    return header, seq

def revcomp(seq: str):
    conv = {"A": "T", "G": "C", "C": "G", "T": "A"}
    return "".join([conv[s] for s in seq[::-1]])


# INPUT -------------------------------------------

file_in = "sample/dataset/pmch.txt"
file_out = "sample/output/pmch.txt"

with open(file_in) as f:
    data = f.read().splitlines()

with open(file_out) as f:
    outcome = f.read().splitlines()

file_in = "case/dataset/pmch.txt"

with open(file_in) as f:
    data_case = f.read().splitlines()

if not data_case == []:
    data = data_case

# MAIN -------------------------------------------
_, seq = fmtfa(data)

seq = seq[0]

from math import factorial

a = 0
g = 0
for s in seq:
    if s == "A":
        a += 1
    if s == "G":
        g += 1

ans = str(factorial(a) * factorial(g))

# OUTPUT -------------------------------------------

with open("case/output/pmch.txt", "w") as f:
    f.write(ans)

# END
