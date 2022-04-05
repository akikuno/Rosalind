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


# N = len(seq)

# # seq1= "TGGAATCGGAAATCTCTCTGAAAATTTTCTTCTGTTGGAAGATACTTCTT"
# seq_mut = []
# for i in range(N):
#     seq_diff = 0
#     pos = list()
#     for j in range(N):
#         seq1 = seq[i]
#         seq2 = seq[j]
#         x1 = hamming_pos(seq1, seq2)
#         x2 = hamming_pos(seq1, revcomp(seq2))
#         if len(x1) == 1:
#             pos.append(x1[0])
#         if len(x2) == 1:
#             pos.append(x2[0])
#     if len(pos) == 1:
#         seq_mut.append((seq1, pos[0]))

# set(seq_mut)

# ans = set()
# for seq1 in seq_mut:
#     for seq2 in seq:
#         if hamming_dist(seq1, seq2) == 1:
#             for idx, (s1, s2) in enumerate(zip(seq1, seq2)):
#                 if s1 != s2:
#                     nt_index = [s2, idx]
#         elif hamming_dist(seq1, revcomp(seq2)) == 1:
#             for idx, (s1, s2) in enumerate(zip(seq1, revcomp(seq2))):
#                 if s1 != s2:
#                     nt_index = [s2, idx]
#     seq_correct = list(seq1)
#     nt, idx = nt_index
#     seq_correct[idx] = nt
#     seq_correct = "".join(seq_correct)
#     ans.add(f"{seq1}->{seq_correct}")

# def mut_index(seq1, seq2):
#     revseq2 = revcomp(seq2)
#     if seq1 == seq2 or seq1 == revseq2:
#         return
#     mut_s2 = []
#     mut_s2_count = 0
#     for idx, (s1, s2) in enumerate(zip(seq1, seq2)):
#         if s1 != s2:
#             mut_s2.append((s2, idx))
#             mut_s2_count += 1
#     mut_s2r = []
#     mut_s2r_count = 0
#     for idx, (s1, s2r) in enumerate(zip(seq1, revseq2)):
#         if s1 != s2r:
#             mut_s2r.append((s2r, idx))
#             mut_s2r_count += 1
#     if mut_s2_count == 1:
#         return mut_s2[0]
#     if mut_s2r_count == 1:
#         return mut_s2r[0]



# N = len(seq)

# ans = set()
# visited = set()
# for i in range(N):
#     for j in range(i, N):
#         seq1 = seq[i]
#         seq2 = seq[j]
#         if revcomp(seq1) in visited:
#             continue
#         if mut_index(seq1, seq2):
#             mut, idx = mut_index(seq1, seq2)
#             s = list(seq1)
#             s[idx] = mut
#             s = "".join(s)
#             ans.add(f"{seq1}->{s}")
#             visited.add(seq1)

ans = "\n".join(ans)
# OUTPUT -------------------------------------------

with open("case/output/corr.txt", "w") as f:
    f.write(ans)

# END
