import sys, copy
input = sys.stdin.readline


def dfs(dx, dy, s):
    global MAX
    if dy >= M - 1:
        dx += 1
        dy = 0
    if dx >= N - 1:
        MAX = max(MAX, s)
        return

    for Next in [PASS, s1, s2, s3, s4]:
        if Next == PASS:
            dfs(dx, dy + 1, s)
        else:
            F = True
            ts = 0
            for k in range(2):
                for l in range(2):
                    if Next[k][l] != 0:
                        if F and Next[k][l] * tboard[dx + k][dy + l] != 0:
                            ts += Next[k][l] * tboard[dx + k][dy + l]
                        else:
                            F = False
                            ts = 0
            if F:
                for k in range(2):
                    for l in range(2):
                        if Next[k][l] != 0:
                            tboard[dx + k][dy + l] = 0
                dfs(dx, dy + 1, s + ts)
                for k in range(2):
                    for l in range(2):
                        if Next[k][l] != 0:
                            tboard[dx + k][dy + l] = board[dx + k][dy + l]


N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

PASS = True
s1 = [[1, 2], [0, 1]]
s2 = [[0, 1], [1, 2]]
s3 = [[1, 0], [2, 1]]
s4 = [[2, 1], [1, 0]]

MAX = 0
tboard = copy.deepcopy(board)
dfs(0, 0, 0)

print(MAX)
