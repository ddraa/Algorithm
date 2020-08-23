import sys
N = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))
h = {}
for k in li:
    if k not in h:
        h[k] = 1
    else:
        h[k] += 1
M = int(sys.stdin.readline())
ok = list(map(int, sys.stdin.readline().split()))

for s in ok:
    if s in h:
        print(h[s],end= " ")
    else:
        print(0, end = " ")
