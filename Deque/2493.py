import sys

N = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))
index = {}
stack, ans = [], []
for i in range(N):
    index[l[i]] = i + 1

for i in range(N):
    while stack and l[i] > stack[-1]:
        stack.pop()

    if stack:
        ans.append(index[stack[-1]])
        stack.append(l[i])
    else:
        stack.append(l[i])
        ans.append(0)
print(*ans)



