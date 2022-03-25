import math

file = "data/rosalind_prob.txt"
seq = "TATAAGAACATACCAGCACGTGGAGCTTTAGTGGCCCCAACCCGCTCACATTTGGTTTCCACTTAAGCGGTTTCCAACCCCGCTCTCCGACCGTCG"
GC = [0.102, 0.135, 0.178, 0.267, 0.299, 0.374, 0.424, 0.476, 0.547, 0.606, 0.655, 0.703, 0.733, 0.800, 0.883, 0.907]

num_AT = seq.count("A")
num_AT += seq.count("T")
num_GC = seq.count("G")
num_GC += seq.count("C")

ans = []
for x in GC:
    gcp = x / 2
    atp = (1 - x) / 2
    ans.append(math.log10(gcp ** num_GC) + math.log10(atp ** num_AT))

print(*ans)
