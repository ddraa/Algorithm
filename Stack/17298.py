import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
stack = []
res = [-1 for _ in range(N)]

for i in range(N):
    while stack and arr[stack[-1]] < arr[i]:
        res[stack.pop()] = arr[i]
    stack.append(i)
print(*res)