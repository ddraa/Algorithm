import sys

L = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
for N in range(11, 101):
    L.append(L[N - 1] + L[N - 5])

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    print(L[N])