from pathlib import Path

# https://rosalind.info/problems/dna/

# SAMPLE INPUT -------------------------------------------

sample_dataset = Path("sample/dataset/dna.txt").read_text().splitlines()
sample_output = Path("sample/output/dna.txt").read_text().splitlines()

# DATASET INPUT -------------------------------------------

dataset = Path("case/dataset/dna.txt").read_text().splitlines()

# MAIN -------------------------------------------

from collections import Counter

c = Counter(dataset[0])

ans = " ".join([str(c[k]) for k in "ACGT"])

# OUTPUT -------------------------------------------

Path("case/output/dna.txt").write_text(ans)

# END
