#!/usr/bin/python3
import sys


def main(*argv):
    arg_count = len(sys.argv)
    sum = 0
    if arg_count > 1:
        for args in sys.argv:
            if args != sys.argv[0]:
                sum = sum + int(args)
    print(sum)


if __name__ == "__main__":
    main()
