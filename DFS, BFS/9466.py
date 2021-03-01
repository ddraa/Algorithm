import sys
sys.setrecursionlimit(10 ** 6)


def dfs(st, pick):
    global c

    stack.append(st)

    if not visited[pick]:
        visited[pick] = True
        dfs(pick, stu[pick])

    if not used[pick]:
        cycle = set()
        for index in range(stack.index(pick), len(stack)):
            cycle.add(stack[index])
        while stack:
            k = stack.pop()
            used[k] = True
            if k not in cycle:
                c += 1
    else:
        while stack:
            k = stack.pop()
            used[k] = True
            c += 1

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    stu = list(map(int, sys.stdin.readline().split()))
    used = {}
    visited = [False for _ in range(N)]
    for i in range(N):
        stu[i] -= 1
        used[i] = False
    stack = []
    c = 0

    for i, s in enumerate(stu):
        if not visited[i]:
            visited[i] = True
            dfs(i, s)
    print(c)