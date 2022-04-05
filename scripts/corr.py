# https://rosalind.info/problems/corr/


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

file_in = "sample/dataset/corr.txt"
file_out = "sample/output/corr.txt"

with open(file_in) as f:
    data = f.read().splitlines()

with open(file_out) as f:
    outcome = f.read().splitlines()

file_in = "case/dataset/corr.txt"

with open(file_in) as f:
    data_case = f.read().splitlines()

if not data_case == []:
    data = data_case

# MAIN -------------------------------------------

_, seq = fmtfa(data)

seq_rev = [revcomp(s) for s in seq]

seq_all = seq + seq_rev
import collections

from numpy import hamming

C = collections.Counter(seq_all)
num = sum(1 for c in C.values() if c == 1) // 2

seq_mut = []
for k,v in C.items():
    if v == 1 and num > 0:
        seq_mut.append(k)
        num -= 1


def hamming_snv(seq1, seq2):
    dist = 0
    pos = 0
    nt = ""
    for idx, (s1, s2) in enumerate(zip(seq1, seq2)):
        if s1 != s2:
            dist += 1
            pos = idx
            nt = s2
    return dist, pos, nt


seq_mut_set = set(seq_mut)
seq_correct = []
for seq1 in seq_mut:
    for seq2 in seq:
        if seq2 in seq_mut_set:
            continue
        dist, pos, nt = hamming_snv(seq1, seq2)
        if dist == 1:
            s = list(seq1)
            s[pos] = nt
            seq_correct.append("".join(s))
            break
        dist, pos, nt = hamming_snv(seq1, revcomp(seq2))
        if dist == 1:
            s = list(seq1)
            s[pos] = nt
            seq_correct.append("".join(s))
            break

ans = []
for seq1, seq2 in zip(seq_mut, seq_correct):
    ans.append(f"{seq1}->{seq2}")


ans = "\n".join(ans)
# OUTPUT -------------------------------------------

with open("case/output/corr.txt", "w") as f:
    f.write(ans)

# END
