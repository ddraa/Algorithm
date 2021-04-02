import sys

N, C = map(int, sys.stdin.readline().split())
M = int(sys.stdin.readline())

state = []
for _ in range(M):
    start, end, count = map(int, sys.stdin.readline().split())
    state.append([start, end, count])

capacity = [C] * (N + 1)
state.sort(key=lambda x: x[1])

res, i = 0, 0

for truck in state:
    source, dest = truck[0], truck[1]
    weight = truck[2]
    for i in range(source, dest):
        weight = min(capacity[i], weight)

    for i in range(source, dest):
        capacity[i] -= weight

    res += weight

print(res)
