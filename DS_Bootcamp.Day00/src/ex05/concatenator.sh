#!/bin/sh

EXPORT="hh_concatenator.csv"

HEADER=$(files=(2025*) 
head -n 1 "${files[0]}" )

echo $HEADER > $EXPORT

for file in 2025*; do
    tail -n +2 $file >> $EXPORT
done