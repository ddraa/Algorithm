def check(matrix, i, j, target, n):
    for a in range(n, 2 * n):
        for b in range(n, 2 * n):
            if matrix[a][b] == target:
                pos_i = a
                pos_j = b
                break
    re_i = pos_i - n
    re_j = pos_j - n
    MIN = float("inf")

    for l in range(3): # *
        for m in range(3):
            t = abs(i - (re_i +l * n)) + abs(j - (re_j + m * n))
            if t < MIN:
                MIN = t
    return MIN


def next_pos(matrix, target, n):
    for a in range(n, 2 * n):
        for b in range(n, 2 * n):
            if matrix[a][b] == target:
                return a, b


def solution(n, board):
    count = 0
    matrix = [] # x 9
    for _ in range(3):
        for b in board:
            matrix.append(3 * b)

    target = 1
    i, j = n, n
    while True:
        count += check(matrix, i, j, target, n)

        tij = next_pos(matrix, target, n)
        i = tij[0]
        j = tij[1]

        target += 1
        if target == n ** 2 + 1:
            break

    return count + n ** 2

print(solution(2, [[1, 2], [4, 3]]	))