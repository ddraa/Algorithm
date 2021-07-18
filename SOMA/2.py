# soma
import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

c = 0
for start in range(N): # start
    curIndex = start

    visited = [0 for _ in range(N)]
    visited[curIndex] += 1 # first visit
    MAX = 0

    while True:
        nextIndex = curIndex + arr[curIndex]
        if not visited[nextIndex]:
            visited[nextIndex] += 1
            curIndex = nextIndex # next step
        else: # repeat check
            p = nextIndex # repeat start index
            c = 1
            curIndex = p + arr[p] # next
            while curIndex != p:
                c += 1
                curIndex = curIndex + arr[curIndex] # next step
            break

    if c > MAX:
        MAX = c
print(MAX)