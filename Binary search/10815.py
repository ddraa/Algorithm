import sys

N = int(sys.stdin.readline())
li = set(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
ok = list(map(int, sys.stdin.readline().split()))


for i in range(M):
    if ok[i] in li:
        print(1, end = " ")
    else:
        print(0, end = " ")