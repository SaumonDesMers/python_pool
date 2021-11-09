from time import sleep

bar = 'ETA: 0.0s [{:>3.0f}%][{:<20}] {}/{} | elapsed time 0.0s'
# ETA: 8.67s [ 23%][=====> ] 233/1000 | elapsed time 2.33s


def ft_progress(list):
    size = len(list) - 1
    for x in list:
        print('\r' + bar.format(x / size * 100, "=" * int(x / size * 20), x, size), end='')
        yield x


list = range(100)
ret = 0
for elem in ft_progress(list):
    ret += elem
    sleep(0.05)
print()
print(ret)
