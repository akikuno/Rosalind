# https://rosalind.info/problems/pdst/


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

file_in = "sample/dataset/pdst.txt"
file_out = "sample/output/pdst.txt"

# file_in = "case/dataset/pdst.txt"

with open(file_in) as f:
    data = f.read().splitlines()

with open(file_out) as f:
    outcome = f.read().splitlines()


# MAIN -------------------------------------------


# OUTPUT -------------------------------------------

with open("case/output/pdst.txt", "w") as f:
    f.write()

# END
