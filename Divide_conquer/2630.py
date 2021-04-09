import sys

def divide(x, y, n):
    global blue, white
    flag = board[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            if board[i][j] != flag:
                divide(x, y, n//2)
                divide(x + n//2, y, n//2)
                divide(x, y + n//2, n//2)
                divide(x + n//2, y + n//2, n//2)
                return

    if flag == 1:
        blue += 1
    else:
        white += 1


N = int(sys.stdin.readline())
board = []
blue, white = 0, 0
for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))

divide(0, 0, N)
print(white)
print(blue)