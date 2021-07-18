# soma divide and conquer

import sys

N = int(sys.stdin.readline())
board = []

for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))
flag = N * N

curx, cury = 0, 0
Len = N
#while flag // 2 != 0:
    # section 나누기

    # 1. Len의 절반만큼 가로줄이기

    # 2. Len의 절반만큼 가로 줄여서 y축 이동

    # 3. Len의 절반만큼 세로줄이기

    # 4. Len의 절반만큼 세로줄여서 x축 이동
