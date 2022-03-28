# https://rosalind.info/problems/pper/

from math import factorial


def P(n, r):
    return factorial(n) // factorial(n - r) % 1_000_000


n, k = 21, 7

P(n, k)
