# https://rosalind.info/problems/tree/

# INPUT -------------------------------------------

file_in = "sample/dataset/tree.txt"
file_out = "sample/output/tree.txt"

with open(file_in) as f:
    data = f.read().splitlines()

with open(file_out) as f:
    outcome = f.read().splitlines()

file_in = "case/dataset/tree.txt"

with open(file_in) as f:
    data_case = f.read().splitlines()

if not data_case == []:
    data = data_case

# MAIN -------------------------------------------

N = int(data[0])

# Disjoint set

import sys

sys.setrecursionlimit(10**9)

par = [-1] * (N)
rank = [0] * (N)
siz = [1] * (N)


def root(x):
    if par[x] == -1:
        return x
    par[x] = root(par[x])
    return par[x]


def unite(x, y):
    rx = root(x)
    ry = root(y)
    if rx == ry:
        return
    if rank[ry] > rank[rx]:
        rx, ry = ry, rx
    par[ry] = rx
    if rank[rx] == rank[ry]:
        rank[rx] += 1


AB = []
for i in range(1, len(data)):
    a, b = [int(x) for x in data[i].split()]
    a -= 1
    b -= 1
    AB.append([int(a), int(b)])


for a, b in AB:
    unite(a, b)

ans = 0
for v in range(N):
    if root(v) == v:
        ans += 1

ans -= 1
ans = str(ans)

# OUTPUT -------------------------------------------

with open("case/output/tree.txt", "w") as f:
    f.write(ans)

# END
