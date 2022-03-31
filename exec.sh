#!/bin/bash

problem="edit"

cat misc/template.py | sed "s|XXXXX|${problem}|g" >scripts/"$problem".py
code . scripts/"$problem".py case/dataset/"$problem".txt case/output/"$problem".txt
