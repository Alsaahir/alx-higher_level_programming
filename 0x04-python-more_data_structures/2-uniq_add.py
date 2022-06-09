#!/usr/bin/python3


def uniq_add(my_list=[]):
    new = []
    sum = 0
    i = 0
    for x in my_list:
        if x not in new:
            new.append(x)

    while i < len(new):
        sum += new[i]
        i += 1
    return (sum)
