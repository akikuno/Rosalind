from itertools import product

file = "data/rosalind_lexf.txt"
with open(file) as f:
    tmp = f.read().splitlines()

seq = tmp[0].split()
num = int(tmp[1])

for a in product(seq, repeat=num):
    print("".join(a))

