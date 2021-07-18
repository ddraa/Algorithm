import sys

input = sys.stdin.readline


def find(u):
    if u != p[u]:
        p[u] = find(p[u])
    return p[u]


def union(u, v):
    r1, r2 = find(u), find(v)
    p[r2] = r1


N = int(input())
graph, p = [], [i for i in range(N)]
total, cost, e = 0, 0, 0

for i in range(N):
    t = input().strip()
    for j in range(N):
        if 'a' <= t[j] <= 'z':
            w = ord(t[j]) - ord('a') + 1
            graph.append((i, j, w))
            total += w
        elif 'A' <= t[j] <= 'Z':
            w = ord(t[j]) - ord('A') + 27
            graph.append((i, j, w))
            total += w

graph.sort(key=lambda x: x[2])

if N == 1:
    if graph:
        print(graph[0][2])
    else:
        print(0)
else:
    for a, b, w in graph:
        if find(a) != find(b):
            union(a, b)
            cost += w
            e += 1
            if e == N - 1:
                print(total - cost)
                break
    else:
        print(-1)
