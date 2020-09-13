opx = [-1,0,1,0]
opy = [0,1,0,-1]

def dfs(maze):
    stack = [[0, 0, 0]]
    N = len(maze)
    visited = [[0]*N for _ in range(N)]
    visited[0][0] = 1

    while stack:
        ax, ay, count = stack.pop()
        if ax == N - 1 and ay == N - 1:
            print(count)
            return count

        for k in range(4):
            x = ax + opx[k]
            y = ay + opy[k]

            if 0<=x<=N-1 and 0<=y<=N-1 and not visited[x][y]:
                if maze[x][y] == 0:
                    visited[x][y] = 1
                    stack.append([x, y, count + 1])


def solution(maze):
    answer = 0
    return dfs(maze)

solution([[0, 1, 0, 1], [0, 1, 0, 0], [0, 0, 0, 0], [1, 0, 1, 0]])