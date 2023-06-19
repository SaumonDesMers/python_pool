import sys


def main():
    if len(sys.argv) != 2 or sys.argv[1].isdigit() is False:
        print("ERROR")
        return
    arg = sys.argv[1]
    if int(arg) == 0:
        print("I'm Zero")
    elif int(arg) % 2 == 0:
        print("I'm Even")
    else:
        print("I'm Odd")


main()
