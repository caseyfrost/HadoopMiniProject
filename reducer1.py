#! /usr/bin/python
import sys

vin_dict = {}
current_vin = None
vin_list = []


def reset():
    global vin_dict
    global current_vin
    global vin_list

    vin_dict = {}
    current_vin = None
    vin_list = []


def flush():
    global vin_dict
    global current_vin
    global vin_list

    for vals in vin_list:
        if vals[0] == 'A':
            print '{}\t("{}", "{}", "{}")'.format(current_vin, vals[0], vin_dict[current_vin][1],
                                                  vin_dict[current_vin][2])
        else:
            continue


for line in sys.stdin:
    # parse input from mapper
    map_data = line.split('\t')
    vin = map_data[0]
    vin_vals = eval(map_data[1])

    if vin_vals[0] == 'I':
        vin_dict[vin] = vin_vals

    if current_vin != vin:
        if current_vin:
            flush()
        reset()

    vin_list.append(vin_vals)
    current_vin = vin

flush()
