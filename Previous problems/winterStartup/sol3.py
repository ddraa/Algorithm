from _collections import deque

dx = [1,-1,0,0]
dy = [0,0,-1,1]

def bfs(matrix, visited, i, j, N, area):
    queue = deque()
    queue.append([i, j])
    while queue:
        ax, ay = queue.popleft()
        for k in range(4):
            kx = ax + dx[k]
            ky = ay + dy[k]
            if 0 <= kx < N and 0 <= ky < N and not visited[kx][ky]:
                if matrix[kx][ky] == area:
                    visited[kx][ky] = 1
                    queue.append([kx, ky])


def solution(v):
    N = len(v)
    answer = []
    visited = [[0] * N for _ in range(N)]
    for k in range(3):
        c = 0
        for i in range(N):
            for j in range(N):
                if not visited[i][j] and v[i][j] == k:
                    visited[i][j] = 1
                    c += 1
                    bfs(v, visited, i, j, N, k)
        answer.append(c)
    return answer

solution([[0,0,1,1],[1,1,1,1],[2,2,2,1],[0,0,0,2]])