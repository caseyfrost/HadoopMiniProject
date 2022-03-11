#! /usr/bin/python
import sys

for line in sys.stdin:
    data = line.strip().split('\t')
    vin_vals = eval(data[1])
    print '{}{}\t1'.format(vin_vals[1], vin_vals[2])
