K, N = map(int, input().split())
c = []
for _ in range(K):
    c.append(int(input()))

l, r = 1, 2**31-1
while l <= r:
    m = (l + r) // 2
    count = 0
    for li in c:
        count += (li // m)
    if count >= N:
        l = m + 1
    else:
        r = m - 1
print(r)