# https://rosalind.info/problems/sset/


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

file_in = "sample/dataset/sset.txt"
file_out = "sample/output/sset.txt"

with open(file_in) as f:
    data = f.read().splitlines()

with open(file_out) as f:
    outcome = f.read().splitlines()

file_in = "case/dataset/sset.txt"

with open(file_in) as f:
    data_case = f.read().splitlines()

if not data_case == []:
    data = data_case

# MAIN -------------------------------------------

n = int(data[0])


from math import factorial

def C(n, r):
    return factorial(n) // (factorial(n - r) * factorial(r))

ans = 0

for i in range(1, n+1):
    ans += C(n, i)
    ans %= 1_000_000

ans += 1

ans = str(ans)
# OUTPUT -------------------------------------------

with open("case/output/sset.txt", "w") as f:
    f.write(ans)

# END
