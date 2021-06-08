import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))


def divide(k):
    c, i = 1, 0
    MIN, MAX = arr[i], arr[i]
    while i < N:
        MAX, MIN = max(MAX, arr[i]), min(MIN, arr[i])
        if MAX - MIN > k:
            c += 1
            MAX, MIN = arr[i], arr[i]
        i += 1

    if c <= M:
        return True
    else:
        return False

l, r = 0, 10 ** 4
while l <= r:
    m = (l + r) // 2
    if divide(m):
        res = m
        r = m - 1
    else:
        l = m + 1
print(res)