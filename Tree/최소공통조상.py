import sys
input = sys.stdin.readline


def dfs(n):
    stack = [n]
    while n != 0:
        stack.append(parent[n])
        n = parent[n]
    return stack


T = int(input())
for _ in range(T):
    N = int(input())
    parent = [0] * (N + 1)

    for _ in range(N - 1):
        a, b = map(int, input().split())
        parent[b] = a

    a, b = map(int, input().split())
    la = dfs(a)
    lb = dfs(b)
    s = la[-1]

    while la and lb:
        a, b = la.pop(), lb.pop()
        if a != b:
            print(s)
            break
        else:
            s = a
    else:
        print(s)
