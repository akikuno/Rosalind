# https://rosalind.info/problems/seto/


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

file_in = "sample/dataset/seto.txt"
file_out = "sample/output/seto.txt"

# file_in = "case/dataset/seto.txt"

with open(file_in) as f:
    data = f.read().splitlines()

with open(file_out) as f:
    outcome = f.read().splitlines()


# MAIN -------------------------------------------


# OUTPUT -------------------------------------------

with open("case/output/seto.txt", "w") as f:
    f.write()

# END
