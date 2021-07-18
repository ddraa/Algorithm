import sys

N, M = map(int, sys.stdin.readline().split())
spend = []
for _ in range(N):
    spend.append(int(sys.stdin.readline()))
l, r = 1, sum(spend)
res = 10 ** 9

while l <= r:
    m = (l + r) // 2

    c, current, up = 0, 0, False
    for i in range(N):
        if spend[i] > m:
            up = True

        if spend[i] > current:
            current = m
            c += 1
        current -= spend[i]

    if up:
        l = m + 1
        continue

    if c > M:
        l = m + 1
    else:
        res = min(res, m)
        r = m - 1
print(res)