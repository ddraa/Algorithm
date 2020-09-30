

def solution(blocks):
    answer = []
    N = len(blocks)
    matrix = [[0]* N for _ in range(N)]
    h = 0
    for i in blocks:
        matrix[h][i[0]] = i[1]
        h += 1

    H = 1

    while H <= N - 1:
        for n in range(H+1): # 각 행의 개수만큼
            if matrix[H][n] != 0:
                idx = n
                break


        l = idx
        while 0 <= l - 1: # left
            matrix[H][l-1] = matrix[H-1][l-1] - matrix[H][l]
            l -= 1

        r = idx
        while r + 1 <= H: # right
            matrix[H][r + 1] = matrix[H-1][r] - matrix[H][r]
            r += 1
        H += 1

    for i in range(N):
        for j in range(i+1):
            answer.append(matrix[i][j])

    return answer


print(solution([[0, 50], [0, 22], [2, 10], [1, 4], [4, -13]]	))