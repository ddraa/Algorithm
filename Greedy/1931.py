import sys

N = int(sys.stdin.readline())
time = []
for _ in range(N):
    time.append(list(map(int, sys.stdin.readline().split())))

time.sort(key=lambda x:(x[1], x[0]))
END_TIME = 0
c = 0
for t in time:
    if t[0] >= END_TIME:
        c += 1
        END_TIME = t[1]
print(c)