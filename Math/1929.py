import sys
M, N = map(int, sys.stdin.readline().split())
a = [False,False] + [True]*(N-1)

for i in range(2, N + 1):
    if a[i]:
        for j in range(2 * i, N + 1, i):
            a[j] = False
        if M <= i <= N:
            print(i)

