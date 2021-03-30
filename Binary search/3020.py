import sys, bisect

N, H = map(int, sys.stdin.readline().split())
up, down = [], []
for i in range(N):
    if i % 2 == 0:
        down.append(int(sys.stdin.readline()))
    else:
        up.append(int(sys.stdin.readline()))

up.sort()
down.sort()
MIN = N
pathCount = 0

for h in range(1, H + 1):
    upCount = N // 2 - bisect.bisect_left(up, H - h + 1)
    downCount = N // 2 - bisect.bisect_left(down, h)
    count = upCount + downCount

    if MIN > count:
        MIN = count
        pathCount = 1
    elif MIN == count:
        pathCount += 1

print(MIN, pathCount)