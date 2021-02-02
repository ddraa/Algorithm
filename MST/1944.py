import sys
from collections import deque

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
inf = 2500
def BFS(rx, ry):
    queue = deque([[rx, ry, 0]])
    visited = [[False] * N for _ in range(N)]

    while queue:
        X, Y, d = queue.popleft()
        num1, num2 = min(nidx[rx][ry], nidx[X][Y]), max(nidx[rx][ry], nidx[X][Y])
        if mat[X][Y] == 'S' or mat[X][Y] == 'K':
            if (X != rx or Y != ry) and not flag[num1][num2]:
                graph.append([num1, num2, d])
                flag[num1][num2] = True
                continue

        for k in range(4):
            tx, ty = X + dx[k], Y + dy[k]
            if 0 <= tx <= N-1 and 0 <= ty <= N-1 and not visited[tx][ty] and mat[tx][ty] != '1':
                visited[tx][ty] = True
                queue.append([tx, ty, d+1])

def find(u):
    if u != p[u]:
        p[u] = find(p[u])
    return p[u]


def union(u, v):
    r1 = find(u)
    r2 = find(v)
    p[r2] = r1

N, K = map(int, sys.stdin.readline().split())

#init
cost, edges, c = 0, 0, 0 # c : # of nodes
graph, mat, node, nidx = [], [], [], [[-1] * inf for _ in range(inf)]
flag = [[False] * inf for _ in range(inf)]

for _ in range(N):
    mat.append(sys.stdin.readline().strip())

for i in range(N):
    for j in range(N):
        if mat[i][j] == 'S' or mat[i][j] == 'K':
            node.append((i, j))
            nidx[i][j] = c # input node number
            c += 1

p = [i for i in range(inf)]

for x, y in node:
    BFS(x, y)
graph = deque(sorted(graph, key=lambda g:g[2]))

while True:
    if edges == len(node) - 1:
        break
    if not graph:
        print(-1)
        exit(0)
    a, b, w = graph.popleft()
    if find(a) != find(b):
        union(a, b)
        cost += w
        edges += 1
print(cost)