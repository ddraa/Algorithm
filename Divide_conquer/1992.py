import sys

def divide(x, y, n):
    global ans
    flag = board[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            if board[i][j] != flag:
                ans += '('
                for k in range(2):
                    for l in range(2):
                        divide(x + k*n//2, y + l*n//2, n//2)
                ans += ')'
                return

    ans += flag


N = int(sys.stdin.readline())
board = []
for _ in range(N):
    board.append(sys.stdin.readline().strip())
ans = ""
divide(0, 0, N)
print(ans)