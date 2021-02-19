import sys
from collections import deque
t = int(sys.stdin.readline())

def op(n, k):
    if k == 0 : # D
        return (2 * n) % 10000, 'D'
    elif k == 1 : # S
        n -= 1
        return n if n >= 0 else 9999, 'S'
    elif k == 2: # L
        q, r = divmod(n, 1000)
        return r * 10 + q, 'L'
    else:
        q, r = divmod(n, 10)
        return r * 1000 + q, 'R'

def bfs(s, res):
    queue = deque([s])
    visited[s] = res
    while queue:
        s = queue.popleft()
        if s == B:
            return visited[s]

        for i in range(4):
            next_, r = op(s, i)
            if next_ not in visited:
                visited[next_] = visited[s] + r
                queue.append(next_)

for _ in range(t):
    visited = {}
    A, B = map(int, sys.stdin.readline().split())
    print(bfs(A, ""))
