#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    addition = sum([x * y for x, y in my_list])
    res = addition / sum([y for x, y in my_list])
    return res
