from itertools import product
import sys

MIN = float('inf')
N = sys.stdin.readline()
i_N = int(N)
_ = int(sys.stdin.readline())
de = sys.stdin.readline().split()
button = list(map(str, range(0, 10)))
for d in de:
    button.remove(d)

for i in range(0, len(N)+1):
    if i == 0: # only + or -
        if MIN > abs(i_N - 100):
            MIN = abs(i_N - 100)
        continue

    products = product(button, repeat=i)

    for p in products:
        i_num = int("".join(p))
        if abs(i_N - i_num) + i < MIN:
            MIN = abs(i_N - i_num) + i


print(MIN)