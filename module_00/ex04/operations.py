import sys


def op(x, y):
    a, b, c = x + y, x - y, x * y
    d = x / y if y != 0 else "ERROR (div by 0)"
    e = x % y if y != 0 else "ERROR (modulo by 0)"
    return a, b, c, d, e


def help():
    print("Usage: python operations.py <number1> <number2>")
    print("Example:")
    print("    python operations.py 10 3")


if len(sys.argv) == 1:
    pass
elif len(sys.argv) == 2:
    print("InputError: not enough arguments\n")
elif len(sys.argv) > 3:
    print("InputError: too many arguments\n")
elif not sys.argv[1].isdigit() or not sys.argv[2].isdigit():
    print("InputError: only numbers\n")
else:
    a, b, c, d, e = op(int(sys.argv[1]), int(sys.argv[2]))

    print("Sum:", a)
    print("Difference:", b)
    print("Product:", c)
    print("Quotient:", d)
    print("Remainder:", e)

    sys.exit()
help()
