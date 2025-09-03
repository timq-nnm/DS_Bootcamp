#!/bin/bash

INPUT="../ex01/hh.csv"

head -n 1 $INPUT > hh_sorted.csv

tail -n 19 $INPUT | sort -t "," -k2,2 -k1,1 >> hh_sorted.csv