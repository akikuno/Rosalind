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

with open(file_in) as f:
    data = f.read().splitlines()

with open(file_out) as f:
    outcome = f.read().splitlines()

file_in = "case/dataset/pdst.txt"

with open(file_in) as f:
    data_case = f.read().splitlines()

if not data_case == []:
    data = data_case

# MAIN -------------------------------------------

_, seq = fmtfa(data)

def dist(seq1, seq2):
    n = len(seq1)
    d = 0
    for i in range(n):
        if seq1[i] != seq2[i]:
            d += 1
    return d / n

n = len(seq)

ans = []
for i in range(n):
    for j in range(n):
        seq1 = seq[i]
        seq2 = seq[j]
        d = dist(seq1, seq2)
        ans.append(d)

tmp = []
for i in range(0, len(ans), n):
    tmp.append(" ".join([str(a) for a in ans[i:i+n]]))

ans = "\n".join(tmp)

# OUTPUT -------------------------------------------

with open("case/output/pdst.txt", "w") as f:
    f.write(ans)

# END
