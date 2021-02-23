import sys

def fac(k):
    if k == 1:
        return k
    else:
        return k * fac(k - 1)

n, m = map(int, sys.stdin.readline().split())
ans = 1
c = 0
while c < m:
    ans *= (n - c)
    c += 1

print(ans // fac(m))

