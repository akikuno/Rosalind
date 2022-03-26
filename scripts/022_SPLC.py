import re

conv = """TTT F      CTT L      ATT I      GTT V
TTC F      CTC L      ATC I      GTC V
TTA L      CTA L      ATA I      GTA V
TTG L      CTG L      ATG M      GTG V
TCT S      CCT P      ACT T      GCT A
TCC S      CCC P      ACC T      GCC A
TCA S      CCA P      ACA T      GCA A
TCG S      CCG P      ACG T      GCG A
TAT Y      CAT H      AAT N      GAT D
TAC Y      CAC H      AAC N      GAC D
TAA Stop   CAA Q      AAA K      GAA E
TAG Stop   CAG Q      AAG K      GAG E
TGT C      CGT R      AGT S      GGT G
TGC C      CGC R      AGC S      GGC G
TGA Stop   CGA R      AGA R      GGA G
TGG W      CGG R      AGG R      GGG G
""".split()

conv = {dna: aa for dna, aa in zip(conv[0::2], conv[1::2])}


def read_fasta(file: str):
    """
    Args
    file: path of fasta file
    """
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
    return header, seq


file = "data/rosalind_splc.txt"
_, seq = read_fasta(file)

seq_split = "|".join(seq[1:])

seq_main = "".join(re.split(f"{seq_split}", seq[0]))

ans = []
flag = False
for i in range(len(seq_main)):
    if seq_main[i : i + 3] != "ATG":
        continue
    ans.append("M")
    for j in range(i + 3, len(seq_main), 3):
        if conv[seq_main[j : j + 3]] == "Stop":
            flag = True
            break
        ans.append(conv[seq_main[j : j + 3]])
    if flag:
        break

print("".join(ans))
