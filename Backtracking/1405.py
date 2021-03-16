import sys

def direct(x, y, op):
    if op == 'E':
        return x, y + 1
    elif op == 'W':
        return x, y - 1
    elif op == 'S':
        return x + 1, y
    else:
        return x - 1, y

def dfs(n, string, x, y, res):
    global ans

    if n == N:
        ans += res
        return

    for Next in "EWSN":
        nx, ny = direct(x, y, Next)
        if not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(n + 1, string + Next, nx, ny, res * dic[Next])
            visited[nx][ny] = False

In = list(map(int, sys.stdin.readline().split()))

N = In[0]
per = In[1:]
dic = {'E' : per[0]/100, 'W' : per[1]/100, 'S' : per[2]/100, 'N' : per[3]/100}
visited = [[False for _ in range(30)] for _ in range(30)]
visited[14][14] = True
ans = 0
dfs(0, "", 14, 14, 1) # start
print(ans)