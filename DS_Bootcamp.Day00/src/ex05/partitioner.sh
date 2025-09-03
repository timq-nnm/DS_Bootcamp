#!/bin/sh

INPUT="../ex03/hh_positions.csv"

HEADER=$(head -n 1 $INPUT)

tail -n 19 $INPUT | cut -d ',' -f 2 | cut -c 2-11 | uniq | while read -r date; do
    EXPORT=${date}.csv
    echo $HEADER > $EXPORT
    tail -n 19 $INPUT | grep $date >> $EXPORT
done