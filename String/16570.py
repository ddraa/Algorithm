import sys

N = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))
MAX = 0
MI = -1
count = [0 for _ in range(N + 1)]
met = [0 for _ in range(N + 1)]

for std in range(N - 2, -1, -1):
    ri = N - 1
    le = std
    c = 0
    while le >= 0 and l[le] == l[ri]:
        c += 1
        le -= 1
        ri -= 1
    if c >= MAX:
        MAX = c
        met[MAX] += 1
print(MAX, met[MAX]) if MAX else print(-1)