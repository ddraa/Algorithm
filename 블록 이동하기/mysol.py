from _collections import deque
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs(board, n):
    queue = deque()
    queue.append([[0,0],[0,1], 0]) # init
    visited = {f'0,0!0,1' : True}
    while queue:
        a, b, count = queue.popleft()
        if (a[0] == n-1 and a[1] == n-1) or (b[0] == n-1 and b[1] == n-1):
            return count


        horizontal = True if a[0] == b[0] else False # 'ㅡ' ?
        #print(a,b,horizontal)
        #print(a, b, count)
        for k in range(4): # moved line
            ax, bx = a[0] + dx[k], b[0] + dx[k]
            ay, by = a[1] + dy[k], b[1] + dy[k]

            if 0<=ax<=n-1 and 0<=ay<=n-1 and 0<=bx<=n-1 and 0<=by<=n-1:
                if f'{ax},{ay}!{bx},{by}' not in visited and board[ax][ay] == 0 and board[bx][by] == 0:
                    visited[f'{ax},{ay}!{bx},{by}'] = True
                    #print(f'{ax},{ay}  {bx},{by} 방')
                    queue.append([[ax,ay],[bx,by], count+1])
        ax = a[0]
        ay = a[1]
        bx = b[0]
        by = b[1]

        if horizontal:
            #print(a, b, " 때 회전!")
            if 0<=ax+1<=n-1:
                if board[ax+1][ay] == 0 and f'{bx},{by}!{bx+1},{by}' not in visited:
                    if 0<=bx<=n-1 and 0<=by<=n-1 and 0<=bx+1<=n-1:
                        if board[bx][by] == 0 and board[bx+1][by] == 0:
                            visited[f'{bx},{by}!{bx+1},{by}'] = True
                            queue.append([[bx, by],[bx+1, by],count+1])
                            #print(bx, by, bx+1, by, count+1)
            if 0<=ax-1<=n-1:
                if board[ax-1][ay] == 0 and f'{bx-1},{by}!{bx},{by}' not in visited:
                    if 0<=bx-1<=n-1 and 0<=by<=n-1 and 0<=bx<=n-1:
                        if board[bx-1][by] == 0 and board[bx][by] == 0:
                            visited[f'{bx-1},{by}!{bx},{by}'] = True
                            queue.append([[bx-1, by],[bx, by],count+1])
            if 0<=bx+1<=n-1:
                if board[bx+1][by] == 0 and f'{ax},{ay}!{ax+1},{ay}' not in visited:
                    if 0<=ax<=n-1 and 0<=ay<=n-1 and 0<=ax+1<=n-1:
                        if board[ax][ay] == 0 and board[ax + 1][ay] == 0:
                            visited[f'{ax},{ay}!{ax+1},{ay}'] = True
                            queue.append([[ax, ay],[ax+1, ay],count+1])
            if 0<=bx-1<=n-1:
                if board[bx-1][by] == 0 and f'{ax-1},{ay}!{ax},{ay}' not in visited:
                    if 0<=ax-1<=n-1 and 0<=ay<=n-1 and 0<=ax<=n-1:
                        if board[ax-1][ay] == 0 and board[ax][ay] == 0:
                            visited[f'{ax-1},{ay}!{ax},{ay}'] = True
                            queue.append([[ax-1, ay],[ax, ay],count+1])
        else: #'ㅣ'
            if 0<=by-1<=n-1:
                if board[bx][by-1] == 0 and f'{ax},{ay-1}!{ax},{ay}' not in visited:
                    if 0<=ax<=n-1 and 0<=ay-1<=n-1 and 0<=ay<=n-1:
                        if board[ax][ay-1] == 0 and board[ax][ay] == 0:
                            visited[f'{ax},{ay-1}!{ax},{ay}'] = True
                            queue.append([[ax, ay-1],[ax, ay],count+1])
            if 0<=by+1<=n-1:
                if board[bx][by+1] == 0 and f'{ax},{ay}!{ax},{ay+1}' not in visited:
                    if 0<=ax<=n-1 and 0<=ay<=n-1 and 0<=ay+1<=n-1:
                        if board[ax][ay] == 0 and board[ax][ay+1] == 0:
                            visited[f'{ax},{ay}!{ax},{ay+1}'] = True
                            queue.append([[ax, ay],[ax, ay+1],count+1])
            if 0<=ay-1<=n-1:
                if board[ax][ay-1] == 0 and f'{bx},{by-1}!{bx},{by}' not in visited:
                    if 0<=bx<=n-1 and 0<=by-1<=n-1 and 0<=by<=n-1:
                        if board[bx][by - 1] == 0 and board[bx][by] == 0:
                            visited[f'{bx},{by-1}!{bx},{by}'] = True
                            queue.append([[bx, by-1],[bx, by],count+1])
            if 0<=ay+1<=n-1:
                if board[ax][ay+1] == 0 and f'{bx},{by}!{bx},{by+1}' not in visited:
                    if 0<=bx<=n-1 and 0<=by<=n-1 and 0<=by+1<=n-1:
                        if board[bx][by] == 0 and board[bx][by+1] == 0:
                            visited[f'{bx},{by}!{bx},{by+1}'] = True
                            queue.append([[bx, by],[bx, by+1],count+1])


def solution(board):
    return(bfs(board,len(board)))

print(solution([[0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 1, 1, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 0]]))