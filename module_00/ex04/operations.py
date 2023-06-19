import sys


if len(sys.argv) == 1:
    print("Usage: python operations.py <number1> <number2>")
    print("Example:")
    print("    python operations.py 10 3")
elif len(sys.argv) == 2:
    print("InputError: not enough arguments")
elif len(sys.argv) > 3:
    print("InputError: too many arguments")
elif not sys.argv[1].isdigit() or not sys.argv[2].isdigit():
    print("InputError: only numbers")
else:
    x, y = int(sys.argv[1]), int(sys.argv[2])

    print("Sum:", x + y)
    print("Difference:", x - y)
    print("Product:", x * y)
    print("Quotient:", x / y if y != 0 else "ERROR (div by 0)")
    print("Remainder:", x % y if y != 0 else "ERROR (modulo by 0)")
