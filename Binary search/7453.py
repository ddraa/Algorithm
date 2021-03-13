import sys

N = int(sys.stdin.readline())
d1, d2 = {}, {}
a, b, c, d = [] ,[] ,[] ,[]

for _ in range(N):
    n1, n2, n3, n4 = map(int, sys.stdin.readline().split())
    a.append(n1)
    b.append(n2)
    c.append(n3)
    d.append(n4)

for i in range(N):
    for j in range(N):
        if a[i] + b[j] not in d1:
            d1[a[i] + b[j]] = 1
        else:
            d1[a[i] + b[j]] += 1

ans = 0
for i in range(N):
    for j in range(N):
        if -(c[i] + d[j]) in d1:
            ans += d1[-(c[i] + d[j])]
print(ans)
