import sys

for line in sys.stdin:
    data = line.strip().split('\t')
    vin_vals = eval(data[1])
    print(f'{vin_vals[1]}{vin_vals[2]}\t1')
