import sys

dx = [-1,1,0,0]
dy = [0,0,-1,1]
R, C = map(int, sys.stdin.readline().split())
matrix = []
for _ in range(R):
    matrix.append(list(sys.stdin.readline().strip()))
MAX = float('-inf')
visited = [0 for _ in range(26)]
visited[ord(matrix[0][0])-ord('A')] = 1 # start

def dfs(x, y, c):
    global MAX
    MAX = max(MAX, c)
    for i in range(4):
        ax = x + dx[i]
        ay = y + dy[i]
        if 0<=ax<R and 0<=ay<C and not visited[ord(matrix[ax][ay])-ord('A')]:
            visited[ord(matrix[ax][ay])-ord('A')] = 1
            dfs(ax,ay,c+1)
            visited[ord(matrix[ax][ay])-ord('A')] = 0


dfs(0, 0, 1)
print(MAX)