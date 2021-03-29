import sys

N, M, L = map(int, sys.stdin.readline().split())
line = list(map(int, sys.stdin.readline().split()))

line.append(0)
line.append(L)
line.sort()

l, r = 1, L
while l <= r:
    m = (l + r)//2

    count = 0
    for index in range(1, N + 2): # N caution
        dist = line[index] - line[index-1]
        count += dist // m
        if dist % m == 0:
            count -= 1

    if count > M:
        l = m + 1
    else:
        res = m
        r = m - 1
print(res)