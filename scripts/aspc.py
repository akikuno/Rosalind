# https://rosalind.info/problems/aspc/


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

file_in = "sample/dataset/aspc.txt"
file_out = "sample/output/aspc.txt"

with open(file_in) as f:
    data = f.read().splitlines()

with open(file_out) as f:
    outcome = f.read().splitlines()

file_in = "case/dataset/aspc.txt"

with open(file_in) as f:
    data_case = f.read().splitlines()

if not data_case == []:
    data = data_case

# MAIN -------------------------------------------

n,m = [int(x) for x in data[0].split()]

# from math import factorial

# def C(n, r):
#     return factorial(n) // (factorial(n - r) * factorial(r))


# ans = 0
# for k in range(m, n+1):
#     ans += C(n, k)
#     ans %= 1000000

# ans = str(ans)

# DP solution

dp = [[0] * (n+1) for _ in range(n+1)]

for i in range(n+1):
    for j in range(n+1):
        if j == 0:
            dp[i][j] = 1
            continue
        if i == j:
            dp[i][j] = dp[i][j-1] + 1
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
        dp[i][j] %= 1_000_000

print(dp[n][n-m])

# OUTPUT -------------------------------------------

with open("case/output/aspc.txt", "w") as f:
    f.write(ans)

# END
