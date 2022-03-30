# https://rosalind.info/problems/lcsq/


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

file_in = "sample/dataset/lcsq.txt"
file_out = "sample/output/lcsq.txt"

file_in = "case/dataset/lcsq.txt"

with open(file_in) as f:
    data = f.read().splitlines()

with open(file_out) as f:
    outcome = f.read().splitlines()


# MAIN -------------------------------------------
_, seq = fmtfa(data)

seq1, seq2 = seq

n = len(seq1)
m = len(seq2)

dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(n + 1):
    for j in range(m + 1):
        if i == 0 or j == 0:
            continue
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        if seq1[i - 1] == seq2[j - 1]:
            dp[i][j] = max(dp[i - 1][j - 1] + 1, dp[i][j])


ans = ""

while n > 0 and m > 0:
    if dp[n][m] == dp[n - 1][m]:
        n -= 1
    elif dp[n][m] == dp[n][m - 1]:
        m -= 1
    else:
        ans += seq1[n - 1]
        n -= 1
        m -= 1

ans = ans[::-1]

# OUTPUT -------------------------------------------

with open("case/output/lcsq.txt", "w") as f:
    f.write(ans)

# END
