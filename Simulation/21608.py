import sys

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def check():
    ans = 0
    for i in range(N):
        for j in range(N):
            num = board[i][j]
            c = 0
            for k in range(4):
                nx, ny = i + dx[k], j + dy[k]
                if 0 <= nx < N and 0 <= ny < N:
                    if board[nx][ny] in stu[num]:
                        c += 1

            if c == 0:
                pass
            elif c == 1:
                ans += 1
            elif c == 2:
                ans += 10
            elif c == 3:
                ans += 100
            else:
                ans += 1000
    return ans


def bfs(n):
    MAX = 0
    one = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                c = 0
                for k in range(4):
                    ax, ay = i + dx[k], j + dy[k]
                    if 0 <= ax < N and 0 <= ay < N:
                        if board[ax][ay] in stu[n]:
                            c += 1
                if c > MAX:
                    MAX = c
                    one = [(i, j)]
                elif c == MAX:
                    one.append((i, j))
    if len(one) == 1:
        board[one[0][0]][one[0][1]] = n
        return

    MAX = 0
    two = []
    for x, y in one:
        c = 0
        for k in range(4):
            ax, ay = x + dx[k], y + dy[k]
            if 0 <= ax < N and 0 <= ay < N:  # count adj empty
                if board[ax][ay] == 0:
                    c += 1

        if c > MAX:
            MAX = c
            two = [(x, y)]
        elif c == MAX:
            two.append((x, y))
    if len(two) == 1:
        x, y = two.pop()
        board[x][y] = n
        return

    two.sort(key=lambda t: (t[0], t[1]))
    board[two[0][0]][two[0][1]] = n


N = int(sys.stdin.readline())
stu = {i: set() for i in range(1, N ** 2 + 1)}
board = [[0 for _ in range(N)] for _ in range(N)]

for _ in range(N ** 2):
    l = list(map(int, sys.stdin.readline().split()))
    for i in range(1, 5):
        stu[l[0]].add(l[i])
    bfs(l[0])

print(check())
