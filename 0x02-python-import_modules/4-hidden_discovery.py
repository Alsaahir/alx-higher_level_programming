#!/usr/bin/python3
import hidden_4


def main():
    data = dir(hidden_4)
    for i in range(len(data)):
        if(data[i][0] != '_'):
            print("{}".format(data[i]))


if __name__ == "__main__":
    main()
