import sys

N = int(sys.stdin.readline())
lis = list(map(int, sys.stdin.readline().split()))
budget = int(sys.stdin.readline())

t = sum(lis)
M = max(lis)
if t <= budget:
    print(M)
else:
    l = 0
    r = M
    while l<=r:
        total = 0
        m = (r+l)//2
        for k in lis:
            total += min(m, k)
        if total <= budget: #enough
            l = m+1
        else :
            r = m-1
    print(l-1)
