#!/bin/bash

problem="inod"

cat misc/template.py | sed "s|XXXXX|${problem}|g" >scripts/"$problem".py
code . scripts/"$problem".py case/dataset/"$problem".txt case/output/"$problem".txt
