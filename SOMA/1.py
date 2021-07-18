# soma
from collections import deque

dx = [-1, 1, 0 ,0]
dy = [0, 0, -1, 1]

def isBox():
    queue = deque()
    queue.append(key)
    bvisited[key[0]][key[1]] = True  # init

    while queue:
        x, y = queue.popleft()
        if x == box[0] and y == box[1]:
            return True
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < M and 0 <= ny < N and board[nx][ny] != 1:
                if not bvisited[nx][ny]:
                    bvisited[nx][ny] = True
                    queue.append((nx, ny))
    return False

def isKey():
    queue = deque()
    queue.append(start)
    kvisited[start[0]][start[1]] = True # init

    while queue:
        x, y = queue.popleft()
        if x == key[0] and y == key[1]:
            return True
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < M and 0 <= ny < N and board[nx][ny] != 1:
                if not kvisited[nx][ny]:
                    kvisited[nx][ny] = True
                    queue.append((nx, ny))
    return False

t = int(input())
for _ in range(t):
    board = []
    M, N = map(int, input().split())

    for _ in range(M):
        board.append(list(map(int, input().split())))


    for i in range(M):
        for j in range(N):
            if board[i][j] == 3:
                start = (i, j)
            elif board[i][j] == 4:
                key = (i, j)
            elif board[i][j] == 2: # box
                box = (i, j)

    kvisited = [[False for _ in range(N)] for _ in range(M)]
    bvisited = [[False for _ in range(N)] for _ in range(M)]
    if isKey():
        if isBox():
            print(1)
            continue
    print(0)
