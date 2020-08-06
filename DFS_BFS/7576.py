from _collections import deque

M, N = map(int, input().split())
box = []
days =[]
opx = [-1,1,0,0]
opy = [0,0,-1,1]
ripeNot = False
ripeall = True
day = 0
ripen = 0
for _ in range(N):
    box.append(list(map(int,input().split())))
for __ in range(N):
    days.append([0 for _ in range(M)])
queue = deque()
for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            queue.append([i,j])
            ripen += 1
        elif box[i][j] == 0:
            ripeall = False

def bfs():
    global day
    while queue:

        ax, ay = queue.popleft()

        for k in range(4):
            xx = ax + opx[k]
            yy = ay + opy[k]
            if 0<=xx<=N-1 and 0<=yy<=M-1:
                if box[xx][yy] == 0:
                    queue.append([xx,yy])
                    box[xx][yy] = 1
                    days[xx][yy] = days[ax][ay] + 1
bfs()
for i in range(N):
    for j in range(M):
        if box[i][j] == 0:
            ripeNot = True
            break

if ripeNot:
    print(-1)
elif ripeall:
    print(0)
else:
    m = 0
    for i in range(N):
        if m < max(days[i]):
            m = max(days[i])
    print(m)