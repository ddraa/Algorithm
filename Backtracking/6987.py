import sys
from itertools import combinations
sys.setrecursionlimit(10**8)

def DFS(i):
    global ans
    if i == 15:
        if w.count(0) == 6 and d.count(0) == 6 and l.count(0) == 6:
            ans = 1
        return
    else:
        x, y = com[i]
        if w[x] > 0 and l[y] > 0:
            w[x] -= 1
            l[y] -= 1
            DFS(i + 1)
            w[x] += 1
            l[y] += 1
        if d[x] > 0 and d[y] > 0:
            d[x] -= 1
            d[y] -= 1
            DFS(i + 1)
            d[x] += 1
            d[y] += 1
        if l[x] > 0 and w[y] > 0:
            l[x] -= 1
            w[y] -= 1
            DFS(i + 1)
            l[x] += 1
            w[y] += 1


for _ in range(4):
    ans = 0
    g = list(map(int, input().split()))
    w, d, l = [], [] ,[]
    for k in range(18):
        if k % 3 == 0: w.append(g[k])
        elif k % 3 == 1: d.append(g[k])
        else: l.append(g[k])

    com = list(combinations(range(6), 2)) # A, B
    DFS(0)
    print(ans)