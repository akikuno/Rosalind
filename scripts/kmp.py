# https://rosalind.info/problems/kmp/


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

file_in = "sample/dataset/kmp.txt"
file_out = "sample/output/kmp.txt"

with open(file_in) as f:
    data = f.read().splitlines()

with open(file_out) as f:
    outcome = f.read().splitlines()

file_in = "case/dataset/kmp.txt"

with open(file_in) as f:
    data_case = f.read().splitlines()

if not data_case == []:
    data = data_case

# MAIN -------------------------------------------

_, seq = fmtfa(data)
seq = seq[0]

seqrev = seq[::-1]

ans = []

for i in range(len(seq)):
    tmp = 0
    for j in range(i, len(seq)):
        print(i, j, seqrev[j])
        if seqrev[j] != seq[0]:
            continue
        # if seq[: j - i] != seqrev[i:j][::-1]:
        #     break
        if seq[: j - i] == seqrev[i:j][::-1]:
            tmp = j - i
    ans.append(tmp)

ans = " ".join(map(str, ans[::-1]))

# OUTPUT -------------------------------------------

with open("case/output/kmp.txt", "w") as f:
    f.write(ans)

# END
