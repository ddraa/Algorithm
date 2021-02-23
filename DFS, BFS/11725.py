import sys
sys.setrecursionlimit(10 ** 6)
def dfs(n):
    for child in tree[n]:
        if par[n] == child:
            pass
        else:
            par[child] = n
            dfs(child)

N = int(sys.stdin.readline())
par = {1 : -1} # root
tree = {}

for _ in range(N - 1):
    u, v = map(int, sys.stdin.readline().split())
    if u not in tree:
        tree[u] = [v]
    else:
        tree[u].append(v)
    if v not in tree:
        tree[v] = [u]
    else:
        tree[v].append(u)

dfs(1)
for k in range(2, N + 1):
    print(par[k])