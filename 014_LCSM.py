import sys

# file = "data/sample.fa"
file = sys.argv[-1]


def read_fasta(file: str):
    """
    Args
    file: path of fasta file
    """
    with open(file) as f:
        fa = f.read().splitlines()
    prev = True
    header = []
    seq = []
    for f in fa:
        if ">" in f:
            header.append(f[1:])
            prev = True
        elif prev:
            seq.append(f)
            prev = False
        else:
            seq[-1] += f
    return header, seq


_, seq = read_fasta(file)

seq = [
    "ACGTACGT",
    "AACCGTATA",
]
seq1 = seq[0]
seq2 = seq[1]

n = len(seq1)
m = len(seq2)

dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(n):
    for j in range(m):
        if i == 0 or j == 0:
            dp[i][j] = 0
            continue
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        if seq1[i] == seq2[j]:
            dp[i][j] = max(dp[i - 1][j - 1] + 1, dp[i][j])

dp

