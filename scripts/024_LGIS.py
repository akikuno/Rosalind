inf = 2 ** 63

from bisect import bisect_left


def lis(l):
    n = len(l)
    lisDP = [inf] * n
    indexList = [None] * n
    for i in range(n):
        ind = bisect_left(lisDP, l[i])
        lisDP[ind] = l[i]
        indexList[i] = ind
    targetIndex = max(indexList)
    ans = [0] * (targetIndex + 1)
    for i in range(n - 1, -1, -1):
        if indexList[i] == targetIndex:
            ans[targetIndex] = l[i]
            targetIndex -= 1
    return ans


file = "data/rosalind_lgis.txt"
with open(file) as f:
    tmp = f.read().splitlines()

n, A = tmp
n = int(n)
A = [int(a) for a in A.split()]
B = [a * -1 for a in A]

print(*lis(A))
print(*[b * -1 for b in lis(B)])

