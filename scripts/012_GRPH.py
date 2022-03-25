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

k = 3

ans = []
for i in range(len(seq)):
    for j in range(len(seq)):
        s1 = seq[i]
        s2 = seq[j]
        if s1 == s2:
            continue
        if s1[-k:] == s2[:k]:
            ans.append(" ".join([header[i], header[j]]))

with open("answer/grph.txt", "w") as f:
    f.write("\n".join(ans))

