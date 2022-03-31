# https://rosalind.info/problems/edit/


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

file_in = "sample/dataset/edit.txt"
file_out = "sample/output/edit.txt"

with open(file_in) as f:
    data = f.read().splitlines()

with open(file_out) as f:
    outcome = f.read().splitlines()

file_in = "case/dataset/edit.txt"

with open(file_in) as f:
    data_case = f.read().splitlines()

if not data_case == []:
    data = data_case

# MAIN -------------------------------------------

_, seq = fmtfa(data)

seq1, seq2 = seq

n = len(seq1)
m = len(seq2)

dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(n + 1):
    dp[i][0] = i

for j in range(m + 1):
    dp[0][j] = j


for i in range(1, n + 1):
    for j in range(1, m + 1):
        if seq1[i - 1] == seq2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1]
            continue
        dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + 1)


ans = str(dp[n][m])

# OUTPUT -------------------------------------------

if ans:
    with open("case/output/edit.txt", "w") as f:
        f.write(ans)

# END
