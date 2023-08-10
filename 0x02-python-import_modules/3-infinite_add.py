#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    result = 0

    for index, argument in enumerate(sys.argv[1:], start=1):
        result = result + int(argument)

    print(result)

