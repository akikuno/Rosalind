# https://rosalind.info/problems/dna/


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

file_in = "sample/dataset/dna.txt"
file_out = "sample/output/dna.txt"

file_in = "case/dataset/dna.txt"

with open(file_in) as f:
    data = f.read().splitlines()

with open(file_out) as f:
    outcome = f.read().splitlines()


# MAIN -------------------------------------------

d = {"A": 0, "C": 0, "G": 0, "T": 0}

for x in data[0]:
    d[x] += 1

print(*d.values())

# OUTPUT -------------------------------------------

with open("case/output/dna.txt", "w") as f:
    f.write(" ".join(map(str, d.values())))

# END
