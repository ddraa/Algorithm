import copy
from _collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def resort(mat):
    global W, H
    m = [[0] * W for _ in range(H)]
    for y in range(W):
        x = 0
        temp = []
        while x < H:
            if mat[x][y] != 0:
                temp.append(mat[x][y])
            x += 1
        x = x - len(temp)
        while x < H:
            m[x][y] = temp.pop(0)
            x += 1
    return m

def bfs(h, w, mat):
    global N, W, H
    queue = deque()
    queue.append([h,w, mat])

    while queue:
        x, y, mat = queue.popleft()

        if mat[x][y] == 1:
            mat[x][y] = 0
            continue
        else:
            length = mat[x][y]
            mat[x][y] = 0
            i = 1
            while i < length:
                for k in range(4):
                    ax = x + dx[k]*i
                    ay = y + dy[k]*i
                    if 0<=ax<=H-1 and 0<=ay<=W-1 and mat[ax][ay]:
                        queue.append([ax,ay, mat])
                i += 1
def dfs(mat, i):
    global MAX, N, W, H
    if i == N-1:
        count = 0
        for a in range(H):
            for b in range(W):
                if mat[a][b] != 0: # brick
                    count += 1
        if MAX < count:
            MAX = count
            return

    temp = copy.deepcopy(mat) # save
    for w in range(W):
        h = 0
        while h<H and mat[h][w] == 0: # h, w -> start
            h += 1
        if h == H: # column all '0'
            continue
        bfs(h, w, mat) # go to destroy ! h w
        new_matrix = resort(mat)
        if i == 3:
            for s in new_matrix:
                print(s)
            print("")
            break
        dfs(new_matrix, i+1)
        mat = copy.deepcopy(temp)
        #break





T = int(input())
MAX = float('-inf')
for ll in range(1, T+1):
    N, W, H = map(int, input().split())
    matrix = []
    for _ in range(H):
        matrix.append(list(map(int, input().split())))

    dfs(matrix, 0)