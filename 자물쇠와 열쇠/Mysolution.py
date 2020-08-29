import copy
from _collections import deque

visited = []


def rotation(k):
    after = [[0] * 3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            after[i][j] = k[2 - j][i]
    return after


def inRange(tx, ty):
    if -1 <= tx <= 3 and -1 <= ty <= 3:
        if not (tx == -1 and ty == -1) and not (tx == -1 and ty == 3) \
                and not (tx == 3 and ty == -1) and not (tx == 3 and ty == 3):
            return True
    return False


def bfs(key, lock):
    N = len(key)
    M = len(lock)

    queue = deque()
    visited.append([1, 1])  # visited
    queue.append([1, 1, key])  # init center

    while queue:
        succeed = True
        tx, ty, k = queue.popleft()
        for a in range(3):
            for b in range(3):
                if k[a][b] + lock[a][b] != 1:
                    succeed = False
        if succeed:
            return True

        # push to left
        ax = tx
        ay = ty - 1
        if inRange(ax, ay) and [ax, ay] not in visited:
            visited.append([ax, ay])
            n_matrix = [[0] * 3 for _ in range(3)]
            for i in range(3):
                for j in range(2):
                    n_matrix[i][j] = k[i][j + 1]
            queue.append([ax, ay, n_matrix])

        # push to right
        ax = tx
        ay = ty + 1
        if inRange(ax, ay) and [ax, ay] not in visited:
            visited.append([ax, ay])
            n_matrix = [[0] * 3 for _ in range(3)]
            for i in range(3):
                for j in range(1, 3):
                    n_matrix[i][j] = k[i][j - 1]
            queue.append([ax, ay, n_matrix])

        # push to up
        ax = tx - 1
        ay = ty
        if inRange(ax, ay) and [ax, ay] not in visited:
            visited.append([ax, ay])
            n_matrix = [[0] * 3 for _ in range(3)]
            for i in range(2):
                for j in range(3):
                    n_matrix[i][j] = k[i + 1][j]
            queue.append([ax, ay, n_matrix])

        # push to down
        ax = tx + 1
        ay = ty
        if inRange(ax, ay) and [ax, ay] not in visited:
            visited.append([ax, ay])
            n_matrix = [[0] * 3 for _ in range(3)]
            for i in range(1, 3):
                for j in range(3):
                    n_matrix[i][j] = k[i - 1][j]
            queue.append([ax, ay, n_matrix])

        # rotation
        r_matrix = k
        for l in range(3):
            r_matrix = rotation(r_matrix)
            queue.append([tx, ty, r_matrix])
    return False


def solution(key, lock):
    return bfs(key, lock)