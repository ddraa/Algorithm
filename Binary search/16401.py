import sys

M, N = map(int, sys.stdin.readline().split())
snack = list(map(int, sys.stdin.readline().split()))
l, r = 1, 10 ** 9
res = None
while l <= r:
    m = (l + r) // 2
    c = 0

    for s in snack:
        c += s // m

    if c >= M: # for max ..
        res = m
        l = m + 1
    else:
        r = m - 1
print(res) if res else print(0)