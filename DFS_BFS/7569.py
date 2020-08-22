from _collections import deque
import sys

dk = [1,-1,0,0,0,0]
dj = [0,0,1,-1,0,0]
di = [0,0,0,0,1,-1]
M, N, H = map(int, sys.stdin.readline().split())
matrix = []
days, count = 0, 0
visited = [[[0]*M for _ in range(N)]for __ in range(H)] # caution! Don't use [[[0]*M]*N]*H ..
for _ in range(H):
    temp = []
    for __ in range(N):
        temp.append(list(map(int, sys.stdin.readline().split())))
    matrix.append(temp)
for i in range(H):
    for j in range(N):
        for k in range(M):
            if matrix[i][j][k] == 1 :
                count += 1


def bfs():
    while queue:
        global days
        x, y, z, day = queue.popleft()
        days = day
        for l in range(6):
            dx = x + di[l]
            dy = y + dj[l]
            dz = z + dk[l]
            if 0<=dx<H and 0<=dy<N and 0<=dz<M:
                if matrix[dx][dy][dz] == 0:
                    matrix[dx][dy][dz] = 1
                    queue.append([dx,dy,dz,day+1])



if count == M*N*H: # all ripen
    print(0)
else:
    non_ripen = False
    queue = deque()
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if matrix[i][j][k] == 1: # all tomatoes can infect adjacent tomatoes Simultaneously (from first day)
                    queue.append([i,j,k,0])
    bfs()
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if matrix[i][j][k] == 0:
                    non_ripen = True
            if non_ripen:
                break
        if non_ripen:
            break

    if non_ripen:
        print(-1)
    else:
        print(days)