import sys

X, Y = map(int, sys.stdin.readline().split())
current_rate = Y * 100 / X

l, r = 1, 10 ** 9
res = None
while l <= r:
    m = (l + r) // 2
    if (Y + m) * 100 // (X + m) > current_rate:
        res = m
        r = m - 1
    else:
        l = m + 1
print(res) if res else print(-1)