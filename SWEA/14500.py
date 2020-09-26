def cal(x, y):
    global MAX
    # ㅡ
    tx = x
    ty = y
    s = 0
    if ty+3 <= M-1:
        k = 0
        while k <= 3:
            s += matrix[tx][ty+k]
            k += 1
        if MAX < s:
            MAX = s

    # ㅣ
    tx = x
    ty = y
    s = 0
    if tx+3 <= N-1:
        k = 0
        while k <= 3:
            s += matrix[tx+k][ty]
            k += 1
        if MAX < s:
            MAX = s

    #
    s = 0
    tx = x
    ty = y
    if tx+1<=N-1 and ty+1 <= M-1:
        s += matrix[tx][ty]
        s += matrix[tx+1][ty]
        s += matrix[tx][ty+1]
        s += matrix[tx+1][ty+1]
        if MAX < s:
            MAX = s


    # L
    s = 0
    tx = x
    ty = y
    if tx + 2 <= N-1 and ty + 1 <= M-1:
        s += matrix[tx][ty]
        s += matrix[tx+1][ty]
        s += matrix[tx+2][ty]
        s += matrix[tx+2][ty+1]
        if MAX < s:
            MAX = s

    #
    s = 0
    tx = x
    ty = y
    if tx + 1 <= N - 1 and ty + 2 <= M - 1:
        s += matrix[tx][ty]
        s += matrix[tx][ty+1]
        s += matrix[tx][ty+2]
        s += matrix[tx+1][ty]
        if MAX < s:
            MAX = s

    # ㄱ
    s = 0
    tx = x
    ty = y
    if tx + 2 <= N - 1 and ty + 1 <= M - 1:
        s += matrix[tx][ty]
        s += matrix[tx][ty + 1]
        s += matrix[tx+1][ty + 1]
        s += matrix[tx + 2][ty+1]
        if MAX < s:
            MAX = s
    #
    s = 0
    tx = x
    ty = y
    if 0<= tx - 1 <= N - 1 and ty + 2 <= M - 1:
        s += matrix[tx][ty]
        s += matrix[tx][ty + 1]
        s += matrix[tx][ty + 2]
        s += matrix[tx -1][ty+2]
        if MAX < s:
            MAX = s

    s = 0
    tx = x
    ty = y
    if 0 <= tx +2 <= N - 1 and ty + 1 <= M - 1:
        s += matrix[tx][ty]
        s += matrix[tx+1][ty]
        s += matrix[tx+1][ty +1]
        s += matrix[tx +2][ty + 1]
        if MAX < s:
            MAX = s

    s = 0
    tx = x
    ty = y
    if 0 <= tx - 1 <= N - 1 and ty + 2 <= M - 1:
        s += matrix[tx][ty]
        s += matrix[tx ][ty+1]
        s += matrix[tx - 1][ty + 1]
        s += matrix[tx - 1][ty + 2]
        if MAX < s:
            MAX = s

    # ㅜ
    s = 0
    tx = x
    ty = y
    if 0 <= tx + 1 <= N - 1 and ty + 2 <= M - 1:
        s += matrix[tx][ty]
        s += matrix[tx][ty + 1]
        s += matrix[tx][ty + 2]
        s += matrix[tx +1][ty + 1]
        if MAX < s:
            MAX = s
    # ㅗ
    s = 0
    tx = x
    ty = y
    if 0 <= tx - 1 <= N - 1 and ty + 2 <= M - 1:
        s += matrix[tx][ty]
        s += matrix[tx][ty + 1]
        s += matrix[tx][ty + 2]
        s += matrix[tx - 1][ty + 1]
        if MAX < s:
            MAX = s

    # ㅏ
    s = 0
    tx = x
    ty = y
    if 0 <= tx + 2 <= N - 1 and ty + 1 <= M - 1:
        s += matrix[tx][ty]
        s += matrix[tx+1][ty ]
        s += matrix[tx+2][ty]
        s += matrix[tx + 1][ty + 1]
        if MAX < s:
            MAX = s

    # ㅓ

    s = 0
    tx = x
    ty = y
    if 0 <= tx + 2<= N - 1 and 0<= ty - 1 <= M - 1:
        s += matrix[tx][ty]
        s += matrix[tx + 1][ty]
        s += matrix[tx + 2][ty]
        s += matrix[tx + 1][ty - 1]
        if MAX < s:
            MAX = s

    s = 0
    tx = x
    ty = y
    if 0 <= tx - 2 <= N - 1 and 0 <= ty + 1 <= M - 1:
        s += matrix[tx][ty]
        s += matrix[tx ][ty+1]
        s += matrix[tx -1][ty+1]
        s += matrix[tx -2][ty +1]
        if MAX < s:
            MAX = s

    # ㄴ

    s = 0
    tx = x
    ty = y
    if 0 <= tx + 1 <= N - 1 and 0 <= ty + 2 <= M - 1:
        s += matrix[tx][ty]
        s += matrix[tx+1][ty]
        s += matrix[tx +1][ty + 1]
        s += matrix[tx + 1][ty + 2]
        if MAX < s:
            MAX = s

    s = 0
    tx = x
    ty = y
    if 0 <= tx + 1 <= N - 1 and 0 <= ty + 2 <= M - 1:
        s += matrix[tx][ty]
        s += matrix[tx ][ty+1]
        s += matrix[tx ][ty + 2]
        s += matrix[tx + 1][ty+2]
        if MAX < s:
            MAX = s


    # ㄱ

    s = 0
    tx = x
    ty = y
    if 0 <= tx + 2 <= N - 1 and 0 <= ty + 1 <= M - 1:
        s += matrix[tx][ty]
        s += matrix[tx + 1][ty]
        s += matrix[tx][ty + 1]
        s += matrix[tx + 2][ty]
        if MAX < s:
            MAX = s

    s = 0
    tx = x
    ty = y
    if 0 <= tx + 2 <= N - 1 and 0 <= ty - 1 <= M - 1:
        s += matrix[tx][ty]
        s += matrix[tx + 1][ty]
        s += matrix[tx+1][ty - 1]
        s += matrix[tx + 2][ty-1]
        if MAX < s:
            MAX = s

    s = 0
    tx = x
    ty = y
    if 0 <= tx + 1 <= N - 1 and 0 <= ty + 2 <= M - 1:
        s += matrix[tx][ty]
        s += matrix[tx][ty+1]
        s += matrix[tx + 1][ty +1]
        s += matrix[tx + 1][ty + 2]
        if MAX < s:
            MAX = s


N, M = map(int, input().split())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))
MAX = float('-inf')
for i in range(N):
    for j in range(M):
        cal(i, j)
print(MAX)