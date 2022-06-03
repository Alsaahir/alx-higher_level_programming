#!/usr/bin/python3
import sys


def main(*argv):
    i = 1
    sum = 0
    while i < len(sys.argv) - 1:
        for args in (sys.argv[i]):
            sum += int(args)
        i += 1
    print(sum)


if __name__ == "__main__":
    main()
