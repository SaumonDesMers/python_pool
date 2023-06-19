import sys

args = sys.argv

if len(args) != 3 or not args[2].isdigit():
    print('Bad argument')
    exit()

for c in '.,?:;!-\'"':
    args[1] = args[1].replace(c, '')
lst = args[1].split()
lst2 = [w for w in lst if len(w) > int(args[2])]
print(lst2)
