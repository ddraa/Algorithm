import sys

N = int(sys.stdin.readline())
building = [int(sys.stdin.readline()) for _ in range(N)]
stack = []
c = 0

for i in range(N):
    while stack and stack[-1] <= building[i]:
        stack.pop()
    if stack:
        c += len(stack)
    stack.append(building[i])
print(c)
