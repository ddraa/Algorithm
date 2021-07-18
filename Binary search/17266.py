import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
pos = list(map(int, sys.stdin.readline().split()))

l, r = 1, 10 ** 5
while l <= r:
    m = (l + r) // 2
    before = 0
    fail = False

    for p in pos:
        if before >= p - m:
            before = p + m
        else:
            fail = True
            break
    if fail:
        l = m + 1
        continue

    if before >= N:
        res = m
        r = m - 1
    else:
        l = m + 1
print(res)