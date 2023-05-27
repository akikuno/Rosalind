from pathlib import Path
# https://rosalind.info/problems/XXXXX/

# SAMPLE INPUT -------------------------------------------

sample_dataset = Path("sample/dataset/XXXXX.txt").read_text().splitlines()
sample_output = Path("sample/output/XXXXX.txt").read_text().splitlines()

# DATASET INPUT -------------------------------------------

dataset = Path("case/dataset/XXXXX.txt").read_text().splitlines()

# MAIN -------------------------------------------

ans = ""

# OUTPUT -------------------------------------------

Path("case/output/XXXXX.txt").write_text(ans)

# END
