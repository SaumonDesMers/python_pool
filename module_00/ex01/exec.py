import sys

arg = sys.argv[1:]
arg = [arg[i][::-1].swapcase() for i in range(len(arg))]
arg.reverse()
print(*arg, sep=' ')
