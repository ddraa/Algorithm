import sys

input = sys.stdin.readline

N = int(input())
F, stack = {}, []
arr = list(map(int, input().split()))
res = [-1 for _ in range(N)]

for n in arr:
    if n in F:
        F[n] += 1
    else:
        F[n] = 1

for i in range(N - 1, -1, -1):
    while stack and stack[-1][0] <= F[arr[i]]:
        stack.pop()

    if stack:
        res[i] = stack[-1][1]
    stack.append((F[arr[i]], arr[i]))
print(*res)
