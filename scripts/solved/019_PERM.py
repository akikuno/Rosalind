from itertools import permutations

N = 5

ans = []
for i in permutations(range(1, N + 1), N):
    ans.append(i)

print(len(ans))
for a in ans:
    print(*a)

