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


def revcomp(seq: str):
    conv = {"A": "T", "G": "C", "C": "G", "T": "A"}
    return "".join([conv[s] for s in seq[::-1]])


# INPUT -------------------------------------------

file_in = "sample/dataset/rear.txt"
file_out = "sample/output/rear.txt"

with open(file_in) as f:
    data = f.read().splitlines()

with open(file_out) as f:
    outcome = f.read().splitlines()

file_in = "case/dataset/rear.txt"

with open(file_in) as f:
    data_case = f.read().splitlines()

if not data_case == []:
    data = data_case

# MAIN -------------------------------------------


def get_reverse_arrays(s: list) -> list[list]:
    reverse_arrays = []
    for left in range(len(s) - 1):
        right = left + 1
        while right < len(s):
            left_flank = s[:left]
            reverse_array = s[left : right + 1][::-1]
            right_flank = s[right + 1 :]
            reverse_arrays.append(left_flank + reverse_array + right_flank)
            right += 1
    return reverse_arrays


def get_reversal_distance(p1: set, p2: set, distance: int) -> int:
    if p1 & p2:
        return distance
    p1_new = set()
    for p in p1:
        reverse_arrays = get_reverse_arrays(list(p))
        for r in reverse_arrays:
            p1_new.add(tuple(r))
    p2_new = set()
    for p in p2:
        reverse_arrays = get_reverse_arrays(list(p))
        for r in reverse_arrays:
            p2_new.add(tuple(r))
    if p1 & p2_new:
        return distance + 1
    if p2 & p1_new:
        return distance + 1
    return get_reversal_distance(p1_new, p2_new, distance + 2)


data = [list(map(int, d.split())) for d in data if d]
ans = []
for i in range(0, len(data), 2):
    a = data[i]
    b = data[i + 1]
    distance, p1, p2 = 0, set(), set()
    p1.add(tuple(data[i]))
    p2.add(tuple(data[i + 1]))
    d = get_reversal_distance(p1, p2, 0)
    ans.append(str(d))

ans = " ".join(ans)

# OUTPUT -------------------------------------------

with open("case/output/rear.txt", "w") as f:
    f.write(ans)

# END
