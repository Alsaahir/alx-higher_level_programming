#!/usr/bin/python3
import sys


def main():
    i = 1
    while i < len(sys.argv) - 1:
        for arg in int(sys.argv[i]):
            arg += int(sys.argv)
        i += 1
    print("{}".format(arg))


if __name__ == "__main__":
    main()
