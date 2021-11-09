import sys


def main():
    if len(sys.argv) == 1:
        return
    arg = sys.argv[1]
    if arg.isdigit() is False or len(sys.argv) > 2:
        print("ERROR")
        return
    if int(arg) == 0:
        print("I'm Zero")
    elif int(arg) % 2 == 0:
        print("I'm Even")
    else:
        print("I'm Odd")


main()
