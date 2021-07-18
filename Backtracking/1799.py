import sys

def check(x, y): # cross check
    tx, ty = x, y
    while tx != 0 and ty != 0:
        tx -= 1
        ty -= 1
        if board[tx][ty] == 'B':
            return False

    tx, ty = x, y
    while tx != N - 1 and ty != N - 1:
        tx += 1
        ty += 1
        if board[tx][ty] == 'B':
            return False

    tx, ty = x, y
    while tx != 0 and ty != N - 1:
        tx -= 1
        ty += 1
        if board[tx][ty] == 'B':
            return False

    tx, ty = x, y
    while tx != N - 1 and ty != 0:
        tx += 1
        ty -= 1
        if board[tx][ty] == 'B':
            return False
    return True


def searchNextIndex(index):
    if N % 2 == 1: # even
        return index + 2
    elif index % N == N - 2:
        return index + 3

    elif index % N == N - 1:
        return index + 1

    else:
        return index + 2


def dfs(current, c):
    global MAX

    if MAX < c:
        MAX = c

    index = current

    while index < N ** 2:
        cx = index // N
        cy = index % N

        if spot[index] == 1:
            if check(cx, cy):
                board[cx][cy] = 'B'
                dfs(searchNextIndex(index), c + 1)
                board[cx][cy] = 1

        index = searchNextIndex(index)


MAX = 0
board, spot = [], []
N = int(sys.stdin.readline())
for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))

for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            spot.append(1)
        else:
            spot.append(0)

dfs(0, 0) # white
wMAX = MAX
MAX = 0
dfs(1, 0) # black

print(wMAX + MAX)