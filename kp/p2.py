





def solution(rows, columns, swipes):
    answer, board = [], []
    i = 1
    for r in range(1, rows + 1):
        t = []
        for c in range(1, columns + 1):
            t.append(i)
            i += 1
        board.append(t)

    for d, x1, y1, x2, y2 in swipes:
        x1 -= 1
        y1 -= 1
        x2 -= 1
        y2 -= 1

        if d == 1:
            t = []
            for j in range(y1, y2 + 1):
                t.append(board[x2][j])

            for i in range(x2, x1, -1):
                for j in range(y1, y2 + 1):
                    board[i][j] = board[i - 1][j]

            answer.append(sum(t))

            for j in range(y2, y1 - 1, -1):
                board[x1][j] = t.pop()

        elif d == 2:
            t = []
            for j in range(y1, y2 + 1):
                t.append(board[x1][j])

            for i in range(x1, x2):
                for j in range(y1, y2 + 1):
                    board[i][j] = board[i + 1][j]

            answer.append(sum(t))

            for j in range(y2, y1 - 1, -1):
                board[x2][j] = t.pop()

        elif d == 3:
            t = []
            for i in range(x1, x2 + 1):
                t.append(board[i][y2])

            for j in range(y2, y1, -1):
                for i in range(x1, x2 + 1):
                    board[i][j] = board[i][j - 1]

            answer.append(sum(t))

            for i in range(x2, x1 - 1, -1):
                board[i][y1] = t.pop()

        else:
            t = []
            for i in range(x1, x2 + 1):
                t.append(board[i][y1])

            for j in range(y1, y2):
                for i in range(x1, x2 + 1):
                    board[i][j] = board[i][j + 1]

            answer.append(sum(t))

            for i in range(x2, x1 - 1, -1):
                board[i][y2] = t.pop()

    return answer




solution(4, 3, [[1, 1, 2, 4, 3], [3, 2, 1, 2, 3], [4, 1, 1, 4, 3], [2, 2, 1, 3, 3]])