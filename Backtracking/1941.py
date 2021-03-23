import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def check():
    queue = deque()
    queue.append(Set[0]) # start
    visited = [False for _ in range(25)]
    visited[Set[0]] = True

    count = 1
    while queue:
        index = queue.popleft()
        tx = index // 5
        ty = index % 5
        for k in range(4):
            nx, ny = tx + dx[k], ty + dy[k]
            Next = nx * 5 + ny
            if 0 <= nx < 5 and 0 <= ny < 5 and not visited[Next]:
                if Next in Set:
                    visited[Next] = True
                    count += 1
                    queue.append(Next)
    if count == 7:
        return True
    else:
        return False


def dfs(c, point, yc):
    global ans
    if yc >= 4:
        return
    if c == 7:
        if check():
            ans += 1
        return


    for cur in range(point, 25): # 순차적, 오름차순적 인덱스 접근법
        x = cur // 5 # 2차원 좌표를 1차원 인덱스로 표현
        y = cur % 5

        Set.append(cur)
        if board[x][y] == 'Y':
            dfs(c + 1, cur + 1, yc + 1)
        else:
            dfs(c + 1, cur + 1, yc)
        Set.remove(cur)


board, Set = [], []
ans = 0
for _ in range(5):
    board.append(list(sys.stdin.readline().rstrip()))

dfs(0, 0, 0)
print(ans)