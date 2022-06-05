#!/usr/bin/python3


def no_c(my_string):
    new_string = []
    for x in my_string:
        if x == "C" or x == "c":
            continue
        else:
            new_string.append(x)
    return (new_string)
