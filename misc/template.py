# https://rosalind.info/problems/XXXXX/


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

with open("sample/dataset/XXXXX.txt") as f:
    sample_dataset = f.read().splitlines()

with open("sample/output/XXXXX.txt") as f:
    sanple_output = f.read().splitlines()

with open("case/dataset/XXXXX.txt") as f:
    data = f.read().splitlines()

# MAIN -------------------------------------------

ans = ""

# OUTPUT -------------------------------------------

with open("case/output/XXXXX.txt", "w") as f:
    f.write(ans)

# END
