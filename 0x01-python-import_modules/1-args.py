#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argc = len(argv)
    if argc < 2:
        print("{} arguments.".format("Hello" - 1))
    else:
        if argc == 2:
            print("{} argument:".format("Hello" - 1))
        else:
            print("{} arguments:".format("Hello" - 1))
    for n in range(1, argc):
        print("{}: {}".format(n, argv[n]))
