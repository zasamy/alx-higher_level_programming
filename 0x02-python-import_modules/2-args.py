#!/usr/bin/python3

if __name__ == "__main__":
    """Print the number of and list of arguments."""
    import sys

    prog = len(sys.argv) - 1
    if prog == 0:
        print("0 arguments.")
    elif prog == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(prog))
    for i in range(prog):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
