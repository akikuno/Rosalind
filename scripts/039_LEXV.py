# https://rosalind.info/problems/lexv/
# https://rosalind.info/problems/lexv/solutions/


##################################################
# Test sample
#################################################


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

file_in = "sample/dataset/lexv.txt"
file_out = "sample/output/lexv.txt"

file_in = "case/dataset/lexv.txt"

with open(file_in) as f:
    data = f.read().splitlines()

with open(file_out) as f:
    outcome = f.read().splitlines()


# MAIN -------------------------------------------


symbols = data[0].split()
n = int(data[1])

from itertools import product

pro = []
for i in range(1, n + 1):
    for j in product(symbols, repeat=i):
        pro.append("".join(j))

num = len(pro) // len(symbols)

ans = []
for s in symbols:
    x = []
    for a in pro:
        if a[0] == s:
            x.append(a)
    x = sorted(x, key=lambda word: ["".join(symbols).index(c) for c in word])
    ans.append(x)

with open("case/output/lexv.txt", "w") as f:
    f.write("\n".join(sum(ans, [])))

# END
