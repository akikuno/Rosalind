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


_, seq = read_fasta("data/rosalind_orf.txt")

start = "ATG"
stops = {"TAG", "TGA", "TAA"}

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

d = {dna: aa for dna, aa in zip(conv[0::2], conv[1::2])}


def return_orf(seq):
    ans = []
    for i in range(len(seq)):
        if seq[i : i + 3] == start:
            tmp = []
            tmp.append(d[start])
            for j in range(i + 3, len(seq), 3):
                if len(seq[j : j + 3]) != 3:
                    break
                if seq[j : j + 3] in stops:
                    tmp.append("X")
                    break
                tmp.append(d[seq[j : j + 3]])
            ans.append("".join(tmp))
    return [a.rstrip("X") for a in ans if "X" in a]


# seq = "AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG"

seq = seq[0]
complement = {"A": "T", "C": "G", "G": "C", "T": "A"}
seq_revcomp = "".join(complement[base] for base in seq[::-1])

ans = return_orf(seq) + return_orf(seq_revcomp)

print(*list(set(ans)), sep="\n")

