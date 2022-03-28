import math

f = math.factorial


def C(n, r):
    return f(n) // (f(n - r) * f(r))


K, N = 6, 16

p = 0.25
q = 1 - p
total = 2 ** K

ans = 0
for i in range(N):
    ans += C(total, i) * pow(p, i) * pow(q, total - i)

print(1 - ans)
