from _collections import deque

dx = [1,0,0,-1]
dy = [0,-1,1,0]
def bfs(pay, a, b, direct, board):
    N = len(board)
    visited_cost = [[float('inf')]*N for _ in range(N)]
    queue = deque()
    queue.append([pay, a, b, direct])

    visited_cost[a][b] = 1
    answer = []
    while queue:
        pay, a, b, direct = queue.popleft()
        if a==N-1 and b == N-1:
            answer.append(pay)

        for k in range(4):
            x = a + dx[k]
            y = b + dy[k]
            if 0<=x<=N-1 and 0<=y<=N-1 and not board[x][y]:
                cur = 1 if a == x else 2 # cur_direct
                if direct == -1 or cur == direct:
                    new_cost = pay + 100
                else:
                    new_cost = pay + 600
                if not visited_cost[x][y] or visited_cost[x][y] >= new_cost:
                    visited_cost[x][y] = new_cost
                    queue.append([new_cost, x, y, cur])

    return answer

def solution(board):
    answer = bfs(0, 0, 0, -1, board)
    print(answer)


solution([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]	)