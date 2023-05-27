# https://rosalind.info/problems/dna/


# DATASET INPUT -------------------------------------------

with open("case/dataset/dna.txt") as f:
    dataset = f.read().splitlines()

# MAIN -------------------------------------------

from collections import Counter

count = Counter(dataset[0])

ans = f'{count["A"]} {count["C"]} {count["G"]} {count["T"]}'

# OUTPUT -------------------------------------------

with open("case/output/dna.txt", "w") as f:
    f.write(ans)

# END
