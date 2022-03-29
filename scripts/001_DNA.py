#################################################
# Test sample
#################################################

file_in = "sample/dataset/sseq.txt"
file_out = "sample/output/sseq.txt"

with open(file_in) as f:
    data = f.read().splitlines()

with open(file_out) as f:
    outcome = f.read().splitlines()


d = {"A": 0, "C": 0, "G": 0, "T": 0}

for s in data[0]:
    d[s] += 1

print(*d.values())
