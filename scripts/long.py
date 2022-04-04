# https://rosalind.info/problems/long/


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

file_in = "sample/dataset/long.txt"
file_out = "sample/output/long.txt"

with open(file_in) as f:
    data = f.read().splitlines()

with open(file_out) as f:
    outcome = f.read().splitlines()

file_in = "case/dataset/long.txt"

with open(file_in) as f:
    data_case = f.read().splitlines()

if not data_case == []:
    data = data_case

# MAIN -------------------------------------------

import re

_, seq = fmtfa(data)

n = len(seq[0])

# Leftmost sequence
for i in range(len(seq)):
    counts = -1
    for j in range(len(seq)):
        if seq[j].count(seq[i][:n//2]):
            counts += 1
    if counts == 0:
        seq_left = seq[i]
        break

# Rightmost sequence
for i in range(len(seq)):
    counts = -1
    for j in range(len(seq)):
        if seq[j].count(seq[i][n//2:]):
            counts += 1
    if counts == 0:
        seq_right = seq[i]
        break


# Append left flang sequences
seq_all = []
visited = [False] * len(seq)

for _ in range(len(seq)):
    for i in range(len(seq_left)//2):
        s = seq_left[i:]
        for idx, ss in enumerate(seq):
            if visited[idx]:
                continue
            if s == seq_left:
                continue
            if re.search(fr"^{s}", ss):
                seq_all.append(seq_left[:i])
                seq_left = ss
                visited[idx] = True
                break

# Append rightmost sequence
seq_all.append(seq_right)

ans = "".join(seq_all)

# OUTPUT -------------------------------------------

with open("case/output/long.txt", "w") as f:
    f.write(ans)

# END
