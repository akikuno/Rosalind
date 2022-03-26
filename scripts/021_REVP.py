def revcomp(seq):
    conv = {"A": "T", "T": "A", "C": "G", "G": "C"}
    return "".join(conv[s] for s in seq[::-1])


seq = "TCAATGCATGCGGGTCTATATGCAT"
ans = []

for i in range(len(seq) + 1):
    for j in range(i + 1, len(seq) + 1):
        s = seq[i:j]
        if not (4 <= len(s) <= 12):
            continue
        if len(s) % 2 == 0:
            if s[: len(s) // 2] == revcomp(s[len(s) // 2 :]):
                ans.append([i + 1, len(s)])

for a in ans:
    print(*a)


seq[: len(seq)]
seq[len(seq)]
