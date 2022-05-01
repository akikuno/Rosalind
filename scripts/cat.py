# https://rosalind.info/problems/cat/


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

file_in = "sample/dataset/cat.txt"
file_out = "sample/output/cat.txt"

with open(file_in) as f:
    data = f.read().splitlines()

with open(file_out) as f:
    outcome = f.read().splitlines()

file_in = "case/dataset/cat.txt"

with open(file_in) as f:
    data_case = f.read().splitlines()

if not data_case == []:
    data = data_case

# MAIN -------------------------------------------


_, seq = fmtfa(data)

seq = seq[0]


def countRNA2Structures(seq):
    if seq in cache:
        return cache[seq]
    tmp = []
    for k in range(1, len(seq), 2):
        tmp.append(countRNA2Structures(seq[1:k]) * cache[seq[0] + seq[k]] * countRNA2Structures(seq[k + 1 :]))
    # assign current sequence into dictionary for later use
    cache[seq] = sum(tmp)
    return cache[seq]


# set up initial dictionary for number of matches for the sequence
cache = {
    "": 1,
    "A": 0,
    "C": 0,
    "G": 0,
    "U": 0,
    "AA": 0,
    "AC": 0,
    "AG": 0,
    "AU": 1,
    "CA": 0,
    "CC": 0,
    "CG": 1,
    "CU": 0,
    "GA": 0,
    "GC": 1,
    "GG": 0,
    "GU": 0,
    "UA": 1,
    "UC": 0,
    "UG": 0,
    "UU": 0,
}

ans = countRNA2Structures(seq) % 10**6

ans = str(ans)
# OUTPUT -------------------------------------------

with open("case/output/cat.txt", "w") as f:
    f.write(ans)

# END
