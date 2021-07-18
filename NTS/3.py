dx = [-1, 1 ,0, 0]
dy = [0, 0, -1, 1]

def solution(board):
    white = []
    for i in range(8):
        for j in range(8):
            if board[i][j] == 2:
                white.append((i, j))
    Next = []
    for w in white:
        x, y = w
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < 8 and 0 <= ny < 8 and board[nx][ny] == 0:
                Next.append((nx, ny))
    MAX = 0

    while Next:
        ans = 0
        bx, by = Next.pop()
        ox, oy = bx, by # save
        board[ox][oy] = 1

        #left
        by -= 1
        c = 0
        while by >= 0 and board[bx][by] == 2:
            c += 1
            by -= 1
        if by >= 0 and board[bx][by] == 1:
            ans += c

        #right
        by = oy
        by += 1
        c = 0
        while by < 8 and board[bx][by] == 2:
            c += 1
            by += 1
        if by < 8 and board[bx][by] == 1:
            ans += c

        # up
        by = oy
        bx -= 1
        c = 0
        while bx >= 0 and board[bx][by] == 2:
            c += 1
            bx -= 1
        if bx >= 0 and board[bx][by] == 1:
            ans += c

        # down
        bx = ox
        bx += 1
        c = 0
        while bx < 8 and board[bx][by] == 2:
            c += 1
            bx += 1
        if bx < 8 and board[bx][by] == 1:
            ans += c


        # left up
        bx = ox
        by = oy
        bx -= 1
        by -= 1
        c = 0
        while bx >= 0 and by >= 0 and board[bx][by] == 2:
            c += 1
            bx -= 1
            by -= 1
        if bx >= 0 and by >= 0 and board[bx][by] == 1:
            ans += c

        # right down
        bx = ox
        by = oy
        bx += 1
        by += 1
        c = 0
        while bx < 8 and by < 8 and board[bx][by] == 2:
            c += 1
            bx += 1
            by += 1
        if bx < 8 and by < 8 and board[bx][by] == 1:
            ans += c

        # left down
        bx = ox
        by = oy
        bx += 1
        by -= 1
        c = 0
        while bx < 8 and by >= 0 and board[bx][by] == 2:
            c += 1
            bx += 1
            by -= 1
        if bx < 8 and by >= 0 and board[bx][by] == 1:
            ans += c

        # right up
        bx = ox
        by = oy
        bx -= 1
        by += 1
        c = 0
        while bx >= 0 and by < 8 and board[bx][by] == 2:
            c += 1
            bx -= 1
            by += 1
        if bx >= 0 and by < 8 and board[bx][by] == 1:
            ans += c

        board[ox][oy] = 0

        if MAX < ans:
            MAX = ans
    return MAX