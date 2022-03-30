# https://rosalind.info/problems/rstr/


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

file_in = "sample/dataset/rstr.txt"
file_out = "sample/output/rstr.txt"

file_in = "case/dataset/rstr.txt"

with open(file_in) as f:
    data = f.read().splitlines()

with open(file_out) as f:
    outcome = f.read().splitlines()


# MAIN -------------------------------------------

n, x = [float(x) for x in data[0].split()]
seq = data[1]

gc = x / 2
at = (1 - x) / 2

prob = 1
for s in seq:
    if s == "A" or s == "T":
        prob *= at
    else:
        prob *= gc

ans = 1 - (1 - prob) ** n


# OUTPUT -------------------------------------------

with open("case/output/rstr.txt", "w") as f:
    f.write(str(ans))

# END
