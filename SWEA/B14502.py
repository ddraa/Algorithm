from _collections import deque
import copy, itertools


dx = [-1,1,0,0]
dy = [0,0,-1,1]


def virus(a, b):
    global MAX, N, M
    queue = deque()
    queue.append([a, b])

    while queue:
        tx, ty = queue.popleft()
        for s in range(4):
            ax = tx + dx[s]
            ay = ty + dy[s]
            if 0<=ax<=N-1 and 0<=ay<=M-1 and not matrix[ax][ay]: # == 0 ?
                matrix[ax][ay] = 2
                queue.append([ax,ay])



N, M = map(int, input().split())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))
wall_list = []
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 0:
            wall_list.append([i,j])
wall_c = 0
MAX = float('-inf')

wall_li = itertools.combinations(wall_list, 3)
temp = copy.deepcopy(matrix)
for idx in wall_li:
    for k in idx:
        x, y = k
        matrix[x][y] = 1 # build wall
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 2: # if virus
                virus(i,j) # spread
    count = 0
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 0:
                count += 1
    if MAX < count:
        MAX = count
    # count the comfort area
    matrix = copy.deepcopy(temp) # reset
print(MAX)