#! /usr/bin/python
import sys

current_key = None
value_list = []


def reset():
    global current_key
    global value_list

    current_key = None
    value_list = []


def flush():
    global current_key
    global value_list

    key_sum = sum(value_list)
    print '{}\t{}'.format(current_key, key_sum)


for line in sys.stdin:
    # parse input from mapper
    map_data = line.split('\t')
    key = map_data[0]
    value = int(map_data[1])

    if current_key != key:
        if current_key:
            flush()
        reset()

    value_list.append(value)
    current_key = key

flush()
