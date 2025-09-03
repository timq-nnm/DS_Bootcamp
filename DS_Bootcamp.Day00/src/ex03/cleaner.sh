#!/bin/bash

INPUT="../ex02/hh_sorted.csv"
EXPORT="hh_positions.csv"

head -n 1 $INPUT > $EXPORT

tail -n 19 $INPUT | awk -F, '{
    position = "";
    
    if ($3 ~ /Junior/) position = "Junior";
    if ($3 ~ /Middle/) position = (position == "" ? "Middle" : position "/Middle");
    if ($3 ~ /Senior/) position = (position == "" ? "Senior" : position "/Senior");
    
    if (position == "") position = "-";
    
    $3 = "\"" position "\"";
    
    print "" $1 "," $2 "," $3 "," $4 "," $5;
}' >> $EXPORT