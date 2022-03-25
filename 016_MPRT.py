# https://rosalind.info/problems/mprt/

import re
import urllib.request

file = "data/sample.txt"
# file = "data/rosalind_mprt.txt"

with open(file) as f:
    ids = f.read().splitlines()

# id = "P07204_TRBM_HUMAN"
ans = []
for id in ids:
    url = f"https://www.uniprot.org/uniprot/{id}.fasta"
    with urllib.request.urlopen(url) as res:
        html = res.read()
        tmp = html.decode()
    seq = "".join(tmp.splitlines()[1:])
    pos = []
    for p in re.finditer(r"(?=N[^P][ST][^P])", seq):
        pos.append(p.start() + 1)
    if not pos:
        continue
    ans.append(id)
    ans.append(" ".join(map(str, pos)))

print(*ans, sep="\n")

# END
