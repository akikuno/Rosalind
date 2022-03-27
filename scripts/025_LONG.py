# https://rosalind.info/problems/long/

file = "data/long.txt"


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


_, seq = read_fasta(file)

# Extract first seq

superstring = ""

if superstring:
    print("hoge")


# END
