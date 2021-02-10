import sys
N = int(sys.stdin.readline())
arr = [int(sys.stdin.readline().rstrip()) for _ in range(N)]
arr.sort()

c, M = 0, 0
p, res = None, arr[0]
for n in arr:
    if n != p:
        if c > M:
            M = c
            res = p
        c = 0
        p = n
    else:
        c += 1
if c > M:
    res = p
print(res)