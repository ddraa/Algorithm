from _collections import deque

dx = [1,0,0,-1]
dy = [0,-1,1,0]
temp = []
C = 0
def bfs(pay, a, b, l_state, board):
    N = len(board)
    visited_cost = [[0]*N for _ in range(N)]
    queue = deque()
    queue.append([pay, a, b, l_state])

    visited_cost[a][b] = 1
    answer = []
    while queue:
        pay, a, b, l_state = queue.popleft()
        if a==N-1 and b == N-1:
            answer.append(pay)

        for k in range(4):
            x = a + dx[k]
            y = b + dy[k]
            if 0<=x<=N-1 and 0<=y<=N-1 and not board[x][y]:
                state = 1 if a != x else 2  # 1 -> vertical
                if l_state == -1 or l_state == state:
                    new_cost = pay + 100
                else:
                    new_cost = pay + 600
                if not visited_cost[x][y] or visited_cost[x][y] > new_cost:
                    visited_cost[x][y] = new_cost
                    queue.append([new_cost, x, y, state])
    for i in visited_cost:
        print(i)
    return temp
def solution(board):
    answer = bfs(0, 0, 0, -1, board)
    for i in answer:
        print(i)


solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]	)