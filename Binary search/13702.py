import sys

N, K = map(int, sys.stdin.readline().split())
al = []
for _ in range(N):
    al.append(int(sys.stdin.readline()))

l, r = 0, 2 ** 31 - 1
res = 0

while l <= r:
    m = (l + r) // 2
    c = 0
    for i in al:
        c += i // m

    if c >= K:
        res = m
        l = m + 1
    else:
        r = m - 1

print(res)