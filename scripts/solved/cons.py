file = input().rstrip()

with open(file) as f:
    fa = f.read().splitlines()

prev = True
header = []
seq = []
for f in fa:
    if ">" in f:
        header.append(f[1:])
        prev = True
    elif prev:
        seq.append(f)
        prev = False
    else:
        seq[-1] += f

A = ["A:"]
C = ["C:"]
G = ["G:"]
T = ["T:"]

from collections import Counter
cons = []
for i in range(len(seq[0])):
    c = Counter()
    d = {"A":0, "C":0, "G":0, "T":0}
    for s in seq:
        c.update(s[i])
    cons.append(c.most_common(1)[0][0])
    for k,v in c.items():
        d[k] = v
    A.append(d["A"])
    C.append(d["C"])
    G.append(d["G"])
    T.append(d["T"])

print("".join(cons))
print(*A)
print(*C)
print(*G)
print(*T)

# counters = list(map(Counter, zip(*seq)))
# consensus = "".join(c.most_common(1)[0][0] for c in counters)
# consensus = "".join(max(c) for c in counters)
# profile_matrix = "\n".join(b + ":" + " ".join(str(c[b]) for c in counters) for b in "ACGT")
# print(*profile_matrix)
# max(c)