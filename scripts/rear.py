# https://rosalind.info/problems/rear/


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

file_in = "sample/dataset/rear.txt"
file_out = "sample/output/rear.txt"

# file_in = "case/dataset/rear.txt"

with open(file_in) as f:
    data = f.read().splitlines()

with open(file_out) as f:
    outcome = f.read().splitlines()


# MAIN -------------------------------------------


def f(seq1, seq2):
    ans = 0
    for i in range(len(seq1)):
        counts = 0
        for j in range(i + 1, len(seq1)):
            if seq1[j] == seq2[j]:
                counts += 1
            if seq1[i] == seq2[j]:
                seq2[i : j + 1] = seq2[i : j + 1][::-1]
                ans += 1
                if counts > 1:
                    seq2[i + 1 : j + 1] = seq2[i : j + 1][::-1]
                    ans += 1
    return ans


data = [d for d in data if d != ""]
n = len(data) // 2

ans = []

for i in range(n):
    seq1 = data[2 * i].split()
    seq2 = data[2 * i + 1].split()
    ans.append(f(seq1, seq2))

print(*ans)
# OUTPUT -------------------------------------------

with open("case/output/rear.txt", "w") as f:
    f.write()

# END
