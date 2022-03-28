import sys

sys.setrecursionlimit(10 ** 6)

n, m = map(int, input().split())


def fib(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n <= m:
        memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    elif n == m + 1:
        memo[n] = fib(n - 1, memo) + fib(n - 2, memo) - 1
    else:
        memo[n] = fib(n - 1, memo) + fib(n - 2, memo) - fib(n - (m + 1), memo)
    return memo[n]


print(fib(n))
