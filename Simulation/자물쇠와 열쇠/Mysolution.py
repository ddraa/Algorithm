def rotation(m):
    N = len(m)
    ret = [[0] * N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            ret[c][N-1-r] = m[r][c]
    return ret


def expand(N, lock):
    expansion = [[0] * 3 * N for _ in range(3 * N)]
    for i in range(N, 2 * N):
        for j in range(N, 2 * N):
            expansion[i][j] = lock[i - N][j - N]
    return expansion

def solution(key, lock):
    answer = True

    M = len(key)
    N = len(lock)

    for _ in range(4):
        key = rotation(key) # rotation
        for i in range(3*N):
            for j in range(3*N):
                succeed = True
                expansion = expand(N, lock) # expansion

                for a in range(M):
                    for b in range(M):
                        if N<=a+i<2*N and N<=b+j<2*N: # in range, cal
                            expansion[a+i][b+j] += key[a][b]

                for x in range(N, 2*N):
                    for y in range(N, 2*N):
                        if expansion[x][y] != 1: # checking
                            succeed = False
                            break
                    if not succeed:
                        break
                if succeed:
                    return True
    return False

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))