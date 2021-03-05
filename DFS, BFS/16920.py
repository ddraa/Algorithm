import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
MAX = 10 ** 6

def spread(p):
    level = 0
    while level < Len[p]:
        C = len(nodes[p])

        for _ in range(C):
            x, y = nodes[p].popleft()
            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == '.':
                    ans[p] += 1
                    nodes[int(p)].append([nx, ny])
                    board[nx][ny] = p + 1
        level += 1


N, M, P = map(int, sys.stdin.readline().split())
Len = list(map(int, sys.stdin.readline().split()))
for i in range(P):
    if Len[i] > MAX:
        Len[i] = MAX

board = []
ans = [0 for _ in range(P)]
nodes = [deque() for _ in range(P)]
for _ in range(N):
    board.append(list(sys.stdin.readline().rstrip()))


for i in range(N):
    for j in range(M):
        if board[i][j] != '.' and board[i][j] != '#':
            board[i][j] = int(board[i][j])
            nodes[int(board[i][j]) - 1].append([i, j]) # make set
            ans[int(board[i][j]) - 1] += 1

while True:
    c = 0
    for i in range(P):
        if not nodes[i]:
            c += 1
        else:
            spread(i)
    if c == P:
        break

for i in range(P):
    print(ans[i], end = " ")