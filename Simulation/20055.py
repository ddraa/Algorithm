import sys

def rotate():
    tright = belt[N - 1]
    dleft = belt[N]

    for j in range(N - 1, 0, -1):
        belt[j] = belt[j - 1]
    for j in range(N, 2 * N - 1):
        belt[j] = belt[j + 1]

    belt[0], belt[-1] = dleft, tright

    for j in range(N - 1, 0, -1):
        robot[j] = robot[j - 1]
    robot[0] = 0
    robot[-1] = 0

N, K = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
robot = [0 for _ in range(N)]
belt = arr[:N] + list(reversed(arr[N:]))
stage = 1

while True:
    rotate()

    for i in range(N - 2, -1, -1):
        if robot[i] == 1 and belt[i + 1] > 0 and robot[i + 1] == 0:
            belt[i + 1] -= 1
            robot[i] = 0
            robot[i + 1] = 1

    robot[-1] = 0

    if robot[0] == 0 and belt[0] > 0:
        belt[0] -= 1
        robot[0] = 1

    if belt.count(0) >= K:
        break
    stage += 1
print(stage)
