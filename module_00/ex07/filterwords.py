import sys

args = sys.argv

if len(args) != 3 or not args[2].isdigit():
    print('Bad argument')
    exit()

for c in '.,?:;!-\'"':
    args[1] = args[1].replace(c, '')
lst = args[1].split()
lst2 = []
for world in lst:
    if len(world) > int(args[2]):
        lst2.append(world)
print(lst2)
