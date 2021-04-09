import sys

def divide(x, y, n):
    global a, b, c
    flag = board[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            if board[i][j] != flag:
                for k in range(3):
                    for l in range(3):
                        divide(x + k*n//3, y + l*n//3, n//3)
                return

    if flag == -1:
        a += 1
    elif flag == 0:
        b += 1
    else:
        c += 1


N = int(sys.stdin.readline())
board = []
a, b, c = 0, 0, 0
for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))

divide(0, 0, N)
print(a)
print(b)
print(c)