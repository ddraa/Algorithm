from _collections import deque
from itertools import combinations
import sys
import copy

opx = [1,-1,0,0]
opy = [0,0,1,-1]
safe = []
zone = []
wall = 0
N, M = map(int, sys.stdin.readline().split())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, list(sys.stdin.readline().split()))))
temp = copy.deepcopy(matrix)

for i in range(N):
    for j in range(M):
        if matrix[i][j] == 0:
            zone.append([i,j])
        elif matrix[i][j] == 1:
            wall += 1
def spread_virus(i,j):

    visit = {}
    queue = deque()
    queue.append([i,j])
    visit[str(i)+str(j)] = True

    while queue:
        ax, ay = queue.popleft()
        for k in range(4):
            xx = ax + opx[k]
            yy = ay + opy[k]

            if 0<=xx<=N-1 and 0<=yy<=M-1:
                if matrix[xx][yy] == 0 and str(xx)+str(yy) not in visit:
                    queue.append([xx,yy])
                    matrix[xx][yy] = 2
                    visit[str(i) + str(j)] = True

permute = combinations(zone,3)
m = 0
for k in permute:
    a, b, c = k[0], k[1], k[2] #index of wall
    matrix[a[0]][a[1]] = 1
    matrix[b[0]][b[1]] = 1
    matrix[c[0]][c[1]] = 1

    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 2:
                spread_virus(i, j)
    count = 0
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 0:
                count += 1

    if m < count:
        m = count
    matrix = copy.deepcopy(temp)
print(m)
