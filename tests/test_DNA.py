#################################################
# Test sample
#################################################

file_in = "sample/dataset/dna.txt"
file_out = "sample/output/dna.txt"

with open(file_in) as f:
    data = f.read().splitlines()

with open(file_out) as f:
    outcome = f.read().splitlines()


d = {"A": 0, "C": 0, "G": 0, "T": 0}

for s in data[0]:
    d[s] += 1

print(*d.values())


def test_sample():
    for s1, s2 in zip(d.values(), outcome[0].split()):
        assert str(s1) == s2


#################################################
# Test case
#################################################

case_in = "case/dataset/dna.txt"


# def test_case():
#     for s1, s2 in zip(d.values(), s_out[0].split()):
#         assert str(s1) == s2

