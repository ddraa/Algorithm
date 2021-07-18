import sys
import math

def make():
    global star

    for i in range(len(star)):
        star.append(star[i] * 2)
        star[i] = ' ' * space + star[i] + ' ' * space

star = ['  *   ', ' * *  ', '***** ']
N = int(sys.stdin.readline())
k = int(math.log2(N//3))
space = 3

for l in range(k):
    make()
    space *= 2
for line in star:
    print(line)