# https://rosalind.info/problems/indc/


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

file_in = "sample/dataset/indc.txt"
file_out = "sample/output/indc.txt"

with open(file_in) as f:
    data = f.read().splitlines()

with open(file_out) as f:
    outcome = f.read().splitlines()

file_in = "case/dataset/indc.txt"

with open(file_in) as f:
    data_case = f.read().splitlines()

if not data_case == []:
    data = data_case

# MAIN -------------------------------------------

import math

N = int(data[0])

math.comb(10, 3) * (1 / 2) ** 10

for n in range(0, 2 * N + 1):
    x = math.comb(2 * N, n) * (1 / 2) ** (2 * n)
    math.log10(x)

math.comb(2 * N, 0)
math.log10((1 / 2) ** (2 * 0.01))

ans = ""

# OUTPUT -------------------------------------------

with open("case/output/indc.txt", "w") as f:
    f.write(ans)

# END
