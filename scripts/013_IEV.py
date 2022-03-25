numbers = list(map(int, input().split()))

expected = [2, 2, 2, 1.5, 1, 0]

ans = 0
for n, e in zip(numbers, expected):
    ans += e * n

print(ans)
