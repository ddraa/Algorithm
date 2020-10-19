
dx = [-1,1,0,0]
dy = [0,0,-1,1]

r, c, T = map(int, input().split())
matrix = []
for _ in range(r):
    matrix.append(list(map(int, input().split())))

clean = []
for i in range(r):
    for j in range(c):
        if matrix[i][j] == -1:
            clean.append([i, j])

for _ in range(T): # T th

    #### spread dust
    spread = {}
    for i in range(r):
        for j in range(c):
            if matrix[i][j] > 0:
                count = 0
                for k in range(4):
                    ax = i + dx[k]
                    ay = j + dy[k]
                    junk = int(matrix[i][j] / 5)
                    if 0<=ax<=r-1 and 0<=ay<=c-1 and matrix[ax][ay] != -1:
                        if f'{ax},{ay}' in spread:
                            spread[f'{ax},{ay}'] += junk
                        else:
                            spread[f'{ax},{ay}'] = junk
                        count += 1
                matrix[i][j] -= junk*count
    for idx in spread:
        x, y = map(int, idx.split(','))
        matrix[x][y] += spread[idx]


    ##### work cleaning
    r_cx,r_cy = clean[0] # upper, save

    cx, cy = r_cx, r_cy
    cx -= 2 # start
    while cx >=0:
        matrix[cx+1][cy] = matrix[cx][cy]
        cx -= 1

    cx += 1
    while cy+1 <= c-1:
        matrix[cx][cy] = matrix[cx][cy+1]
        cy += 1

    while cx+1 <= r_cx:
        matrix[cx][cy] = matrix[cx+1][cy]
        cx += 1

    while cy-1 >= r_cy:
        matrix[cx][cy] = matrix[cx][cy-1]
        cy -= 1
    matrix[cx][cy+1] = 0

    r_cx, r_cy = clean[1]  # lower, save

    cx, cy = r_cx, r_cy
    cx += 1  # start
    while cx + 1 <= r-1:
        matrix[cx][cy] = matrix[cx + 1][cy]
        cx += 1

    while cy + 1 <= c - 1:
        matrix[cx][cy] = matrix[cx][cy + 1]
        cy += 1

    while cx - 1 >= r_cx:
        matrix[cx][cy] = matrix[cx - 1][cy]
        cx -= 1

    while cy - 1 >= r_cy:
        matrix[cx][cy] = matrix[cx][cy - 1]
        cy -= 1
    matrix[cx][cy + 1] = 0

count = 0
for i in range(r):
    for j in range(c):
        if matrix[i][j] != -1:
            count += matrix[i][j]
print(count)