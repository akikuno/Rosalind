# https://rosalind.info/problems/eval/


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

file_in = "sample/dataset/eval.txt"
file_out = "sample/output/eval.txt"

file_in = "case/dataset/eval.txt"

with open(file_in) as f:
    data = f.read().splitlines()

with open(file_out) as f:
    outcome = f.read().splitlines()


file_in = "case/dataset/eval.txt"

with open(file_in) as f:
    data_eval = f.read().splitlines()

if not data_eval == []:
    data = data_eval

# MAIN -------------------------------------------

n = int(data[0])
seq = data[1]
gc_contents = [float(d) for d in data[2].split()]

slot = n - len(seq) + 1

count_nt = [seq.count("A") + seq.count("T"), seq.count("C") + seq.count("G")]

ans = []
for gc in gc_contents:
    p = (gc / 2) ** count_nt[1] * ((1 - gc) / 2) ** count_nt[0] * slot
    ans.append(str(p))

# OUTPUT -------------------------------------------

with open("case/output/eval.txt", "w") as f:
    f.write(" ".join(ans))

# END
