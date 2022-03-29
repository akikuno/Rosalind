import urllib.request
from bs4 import BeautifulSoup
import pathlib

# make directories
pathlib.Path("sample/dataset").mkdir(parents=True, exist_ok=True)
pathlib.Path("sample/output").mkdir(parents=True, exist_ok=True)
pathlib.Path("case/dataset").mkdir(parents=True, exist_ok=True)
pathlib.Path("case/output").mkdir(parents=True, exist_ok=True)
pathlib.Path("scripts").mkdir(parents=True, exist_ok=True)
pathlib.Path("tests").mkdir(parents=True, exist_ok=True)

# Donwload problem lists
url = "https://rosalind.info/problems/list-view/"
with urllib.request.urlopen(url) as res:
    response = res.read()

soup = BeautifulSoup(response, "html.parser")
table = soup.find("table")
tbody = table.find("tbody")
trs = tbody.find_all("tr")

problems = []
for tr in trs:
    p = str(tr.find("td")).replace("<td>", "").replace("</td>", "").lower()
    problems.append(p)

# Download Sample Dataset and Output


def remove_tag(BS4):
    return str(BS4).replace('<div class="codehilite"><pre>', "").replace("</pre></div>", "")


# problem = "gc"
for problem in problems:
    print(problem)
    url = "https://rosalind.info/problems/" + problem
    with urllib.request.urlopen(url) as res:
        response = res.read()
    soup = BeautifulSoup(response, "html.parser")
    # sample
    sample_dataset, sample_output = [remove_tag(s).replace("&gt;", ">") for s in soup.select(".codehilite")][-2:]
    with open(f"sample/dataset/{problem}.txt", "w") as f:
        f.write(sample_dataset)
    with open(f"sample/output/{problem}.txt", "w") as f:
        f.write(sample_output)
    # case
    with open(f"case/dataset/{problem}.txt", "w") as f:
        f.write("")
    with open(f"case/output/{problem}.txt", "w") as f:
        f.write("")
    # scripts
    with open("misc/template.py") as f:
        script = f.read()
    script = script.replace("XXXXX", f"{problem}")
    with open(f"scripts/{problem}.py", "w") as f:
        f.write(script)
