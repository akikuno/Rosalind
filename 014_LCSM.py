# https://rosalind.info/problems/lcsm/
import sys

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


def longest_common_substring(seq1, seq2):
    n = len(seq1)
    m = len(seq2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    index = []
    maxi = 0
    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
                continue
            if seq1[i - 1] == seq2[j - 1]:
                dp[i][j] = max(dp[i - 1][j - 1] + 1, dp[i][j])
                if dp[i][j] == maxi:
                    index.append([i, j])
                if dp[i][j] > maxi:
                    maxi = dp[i][j]
                    index = [[i, j]]
            else:
                dp[i][j] = 0
    results = []
    for idx in index:
        n, m = idx
        tmp_results = ""
        while n > 0 and m > 0:
            if dp[n][m] == 0:
                break
            if dp[n][m] == dp[n - 1][m]:
                n -= 1
            elif dp[n][m] == dp[n][m - 1]:
                m -= 1
            elif dp[n][m] == dp[n - 1][m - 1] + 1:
                tmp_results += seq1[n - 1]
                n -= 1
                m -= 1
        results.append(tmp_results[::-1])
    return results


if len(seq) == 1:
    print(seq[0])
    exit()


seq1 = seq[0]
seq2 = seq[1]
A = longest_common_substring(seq1, seq2)


for i in range(2, len(seq)):
    tmp_A = []
    for a in A:
        tmp_A.append(longest_common_substring(a, seq[i]))
    maxi = 0
    for a in tmp_A:
        if a:
            maxi = max(map(len, a))
    A = []
    for a in tmp_A:
        if a:
            if max(map(len, a)) == maxi:
                A.append(a)
    A = sum(A, [])

print(*A)

####
