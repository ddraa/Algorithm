import sys
input = sys.stdin.readline


def find(u):
    if u != p[u]:
        p[u] = find(p[u])
    return p[u]


def union(u, v):
    r1, r2 = find(u), find(v)
    p[r2] = r1


n, m = map(int, input().split())
p = [i for i in range(n + 1)]
board, graph, res = [], [] , []
c = 0

for _ in range(m):
    x, y = map(int, input().split())
    union(x, y)

for _ in range(n):
    board.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(i + 1, n):
        graph.append((i + 1, j + 1, board[i][j]))
graph.sort(key = lambda k : k[2])

for a, b, w in graph:
    if find(a) != find(b):
        union(a, b)
        c += w
        res.append((a, b))
if c == 0:
    print(0, 0)
else:
    print(c, len(res))
    for r in res:
        print(*r)