import sys
from collections import deque

def bfs(s, e):
    queue = deque()
    queue.append([s, e, 0, 0])

    visited = [[None for _ in range(500_000 + 1)] for _ in range(2)] # 0 even 1 odd
    visited[0][s] = 0

    while queue:
        s, e, sec, state = queue.popleft()
        if visited[state][e] is not None:
            return sec

        Next_state = 0 if (sec + 1) % 2 == 0 else 1
        np = e + sec + 1

        for Next in [s + 1, s - 1, s * 2]:
            if 0 <= Next <= 500_000 and 0 <= np <= 500_000:
                if not visited[Next_state][Next]:
                    visited[Next_state][Next] = sec + 1
                    queue.append([Next, np, sec + 1, Next_state])

    return -1

N, K = map(int, sys.stdin.readline().split())
print(bfs(N, K))