import sys
input = sys.stdin.readline
N = int(input())
k = int(input())

l, r = 1, k
while l <= r:
    m = (l + r) // 2
    c = 0
    for i in range(1, N + 1):
        c += min(N, m // i)
    if c >= k:
        r = m - 1
        ans = m
    else:
        l = m + 1
print(ans)

