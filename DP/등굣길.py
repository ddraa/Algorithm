from collections import deque

def bfs(m, n, board):
    dist = [[0 for _ in range(m)] for _ in range(n)]
    queue = deque()
    queue.append((0, 0, 0))
    count = 0
    while queue:
        x, y, c = queue.popleft()
        if x == n - 1 and y == m - 1:
            count += 1
        if x + 1 < n and board[x + 1][y] != 1 and (not dist[x + 1][y] or dist[x + 1][y] == c + 1):
            dist[x + 1][y] = c + 1
            queue.append((x + 1, y, c + 1))
        if y + 1 < m and board[x][y + 1] != 1 and (not dist[x][y + 1] or dist[x][y + 1] == c + 1):
            dist[x][y + 1] = c + 1
            queue.append((x, y + 1, c + 1))


    return count


def solution(m, n, puddles):
    board = [[0 for _ in range(m)] for _ in range(n)]
    for p in puddles:
        x, y = p
        board[y - 1][x - 1] = 1
    return bfs(m, n, board)


print(solution(4, 3, [[2, 2]]))