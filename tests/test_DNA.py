dataset = "sample/dataset/dna.txt"
output = "sample/output/dna.txt"

with open(dataset) as f:
    data = f.read().splitlines()

with open(output) as f:
    out = f.read().splitlines()


d = {"A": 0, "C": 0, "G": 0, "T": 0}

for s in data[0]:
    d[s] += 1


def test():
    for s1, s2 in zip(d.values(), out[0].split()):
        assert str(s1) == s2

