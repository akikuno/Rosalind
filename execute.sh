#!/bin/bash

usr_name=$(cmd.exe /c "echo %USERNAME%" | tr -d "\r")
mv /mnt/c/Users/"$usr_name"/Downloads/rosa*.txt data

python scripts/rosa.py
###
data/rosalind_grph.txt
###

cp scripts/rosa.py scripts/solved/grph.py
