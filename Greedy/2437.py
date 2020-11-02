import sys
N = int(input())
l = list(map(int, sys.stdin.readline().split()))
l.sort()
s = 0

for i in range(N):
    if s + 1 < l[i]:
        print(s+1)
        break
    else:
        s += l[i]
else:
    print(s + 1)