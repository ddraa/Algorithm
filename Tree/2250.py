import sys
from collections import deque


def findRoot():
    roots = [True for _ in range(N + 1)]
    for i in range(1, N + 1):
        for child in tree[i]:
            if child != -1:
                roots[child] = False
    for i in range(1, N + 1):
        if roots[i]:
            return i


def inOrder(node):
    global c
    if node in tree:
        inOrder(tree[node][0])
        col[node] = c
        c += 1
        inOrder(tree[node][1])


def bfs(node):
    global r
    dq = deque()
    dq.append(node)
    row[node] = r
    level.append(node)

    while dq:
        r += 1
        temp = []
        for _ in range(len(dq)):
            cur = dq.popleft()
            for child in tree[cur]:
                if child != -1:
                    row[child] = r
                    dq.append(child)
                    temp.append(child)
        if temp:
            level.append(temp)


def check():
    MAX = 0
    MAX_LEVEL = 1
    for i in range(2, len(level)):
        if MAX < col[level[i][-1]] - col[level[i][0]]: # guarantee MAX
            MAX = col[level[i][-1]] - col[level[i][0]]
            MAX_LEVEL = i

    print(MAX_LEVEL, MAX + 1)


N = int(sys.stdin.readline())
tree = {i: list() for i in range(1, N + 1)}
col = [None for _ in range(N + 1)]
row = [None for _ in range(N + 1)]
level = [None]

for i in range(1, N + 1):
    n, l, r = map(int, sys.stdin.readline().split())

    tree[n].append(l)
    tree[n].append(r)

root = findRoot()
r, c = 1, 1
inOrder(root)  # col check
bfs(root)  # row check
check()
