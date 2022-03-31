# https://rosalind.info/problems/sign/


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

file_in = "sample/dataset/sign.txt"
file_out = "sample/output/sign.txt"

with open(file_in) as f:
    data = f.read().splitlines()

with open(file_out) as f:
    outcome = f.read().splitlines()

file_in = "case/dataset/sign.txt"

with open(file_in) as f:
    data_case = f.read().splitlines()

if not data_case == []:
    data = data_case

# MAIN -------------------------------------------

n = int(data[0])

from itertools import permutations, product

from math import factorial


def P(n, r):
    return factorial(n) // factorial(n - r)


ans = [str(factorial(n) * 2**n)]
for per in permutations(range(1, n + 1)):
    for pro in product([-1, 1], repeat=n):
        x = [str(a * b) for a, b in zip(per, pro)]
        ans.append(" ".join(x))

ans = "\n".join(ans)
# OUTPUT -------------------------------------------

with open("case/output/sign.txt", "w") as f:
    f.write(ans)

# END
