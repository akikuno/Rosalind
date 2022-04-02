# https://rosalind.info/problems/kmer/


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


# INPUT -------------------------------------------

file_in = "sample/dataset/kmer.txt"
file_out = "sample/output/kmer.txt"

with open(file_in) as f:
    data = f.read().splitlines()

with open(file_out) as f:
    outcome = f.read().splitlines()

file_in = "case/dataset/kmer.txt"

with open(file_in) as f:
    data_case = f.read().splitlines()

if not data_case == []:
    data = data_case

# MAIN -------------------------------------------

_, seq = fmtfa(data)

seq = seq[0]

from itertools import product

kmer = {"".join(x): 0 for x in product(["A", "C", "G", "T"], repeat=4)}

for i in range(len(seq) - 3):
    kmer[seq[i : i + 4]] += 1

ans = [str(v) for v in kmer.values()]
ans = " ".join(ans)
# OUTPUT -------------------------------------------

with open("case/output/kmer.txt", "w") as f:
    f.write(ans)

# END
