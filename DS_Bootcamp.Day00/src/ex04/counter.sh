#!/bin/sh

INPUT="../ex03/hh_positions.csv"
EXPORT="hh_uniq_positions.csv"

echo \"name\",\"count\" > $EXPORT

tail -n 19 $INPUT | cut -d ',' -f3 | sort | uniq -c | awk '{print $2","$1}' >> $EXPORT