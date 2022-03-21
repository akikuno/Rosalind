import sys
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())

def fib(n, memo={}):
    if n in memo: return memo[n]
    if n == 0: return 0
    if n == 1: return 1
    if n <= m:
        memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    elif n == m+1:
        memo[n] = fib(n - 1, memo) + fib(n - 2, memo) - 1
    else:
        memo[n] = fib(n - 1, memo) + fib(n - 2, memo) - fib(n - (m + 1), memo)
    return memo[n]

print(fib(n))

def getChilds(n, m): #find child population Cn
    if (n < 1):
        return 0
    else:
        if (n == 1):
            return 1
        else:
            sumChild = 0
            for i in range(2, m + 1):
                sumChild += getChilds(n - i, m)
            return sumChild

def getPop(n, m): #find current population Fn
    return getChilds(n, m) + getChilds(n + 1, m)

n, m = 6, 3
getPop(n, m)