import sys


def cal(m, day):
    for i in range(1, m):
        if i == 2:
            day += 28
        elif i in [4, 6, 9, 11]:
            day += 30
        else:
            day += 31
    return day


N = int(sys.stdin.readline())
board = []
for _ in range(N):
    a, b, c, d = map(int, sys.stdin.readline().split())
    board.append([cal(a, b), cal(c, d)])

board.sort(key=lambda x: x[0])

start = cal(3, 1)
end = cal(11, 30)
MAX, c = 0, 0

index = 0
Flag = False
while True:
    if index >= N:
        break

    s, e = board[index][0], board[index][1]
    if s <= start:
        if MAX < e:
            MAX = e
            if MAX > end:
                c += 1
                break
            Flag = True
    else:
        if Flag:
            c += 1
            start = MAX
            index -= 1
            Flag = False
    index += 1
print(c) if index < N else print(0)
