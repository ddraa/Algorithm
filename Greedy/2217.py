import sys
N = int(sys.stdin.readline())
li = []
for _ in range(N):
    li.append(int(sys.stdin.readline()))
li.sort()
MAX = float('-inf')

for i in range(len(li)):
    total = li[i] * N
    if MAX < total:
        MAX = total
    N -= 1

print(MAX)