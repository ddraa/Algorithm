import sys

N, M = map(int, sys.stdin.readline().split())
p = []
for _ in range(M):
    p.append(int(sys.stdin.readline()))

l, r = 1, 10 ** 9
res = r

while l <= r:
    m = (l + r) // 2
    c = 0

    for i in range(M):
        c += p[i] // m
        if p[i] % m != 0:
            c += 1

    if c > N:
        l = m + 1
    else:
        res = m # for min ..
        r = m - 1
print(res)