#!/bin/bash

wget -O - https://rosalind.info/problems/list-view/ |
    grep problems |
    grep -v recent |
    grep -v list-view |
    grep -v suggested |
    grep -v RosalindSettings |
    sed "s|.*href||g" |
    awk -F'>' 'NF == 2' |
    sed "s|=\"/problems/||" |
    sed "s|/\">|,|" |
    # add row number starting from 000 to the first column
    awk '{printf "%03d,%s\n", NR-1, $0}' |
    cat >misc/table_id_title.csv
