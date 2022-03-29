#################################################
# Test sample
#################################################


def fmtfa(fasta: list):
    prev = True
    header = []
    seq = []
    for f in fasta:
        if ">" in f:
            header.append(f[1:])
            prev = True
        elif prev:
            seq.append(f)
            prev = False
        else:
            seq[-1] += f
    return header, seq


# INPUT -------------------------------------------

file_in = "sample/dataset/sseq.txt"
file_out = "sample/output/sseq.txt"

# file_in = "case/dataset/sseq.txt"

with open(file_in) as f:
    data = f.read().splitlines()

with open(file_out) as f:
    outcome = f.read().splitlines()


# MAIN -------------------------------------------


_, seq = fmtfa(data)

ans = []
idx = 0
for i, x in enumerate(seq[0]):
    if x == seq[1][idx]:
        ans.append(i + 1)
        idx += 1
    try:
        _ = seq[1][idx]
    except:
        break


print(*ans)


# END
