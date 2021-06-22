import sys
input = sys.stdin.readline


def dfs(c, s, count):
    global MIN
    if count == N:
        if w[c][i] != 0 and MIN > s + w[c][i]:
            MIN = s + w[c][i]
        return

    for adj in range(N):
        if w[c][adj] != 0 and not visited[adj]:
            visited[adj] = True
            dfs(adj, s + w[c][adj], count + 1)
            visited[adj] = False


N = int(input())
w = []
for _ in range(N):
    w.append(list(map(int, input().split())))
MIN = 10 ** 6 * 10

for i in range(N):
    visited = [False] * N
    visited[i] = True
    dfs(i, 0, 1)
print(MIN)