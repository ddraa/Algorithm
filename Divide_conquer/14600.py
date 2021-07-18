import sys


def check(x, y):
    if x == 0 and y == 0:
        return [[1, 2], [2, 1], [2, 2]]
    elif x == 0 and y == 2:
        return [[1, 1], [2, 1], [2, 2]]
    elif x == 2 and y == 0:
        return [[1, 1], [1, 2], [2, 2]]
    else:
        return [[1, 1], [1, 2], [2, 1]]


def divide(x, y, n):
    global color, remain
    if n != 2:
        for k in range(2):
            for l in range(2):
                divide(x + k * n // 2, y + l * n // 2, n // 2)
    else:
        for i in range(2):
            for j in range(2):
                if not (x + i == rx and y + j == ry): # 배수구의 위치가 아닐 경우
                    board[x + i][y + j] = color
                else:
                    remain = check(x, y) # 추가적인 타일 집합 선택
        color += 1


K = int(sys.stdin.readline())
N = 2 ** K
fx, fy = map(int, sys.stdin.readline().split())
rx, ry = N - fy, fx - 1
color = 1
remain = []

board = [[1] * N for _ in range(N)]
board[rx][ry] = -1

if N == 4:
    divide(0, 0, N)
    for a, b in remain:
        board[a][b] = color # 추가적인 타일 집합 색칠

for b in board:
    print(*b)
