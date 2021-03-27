import sys

a, b = [], []
N = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

a.sort()
b.sort(reverse=True)
s = 0
for an, bn in zip(a, b):
    s += an * bn
print(s)