import sys
T = int(sys.stdin.readline())

a = [False,False] + [True] * 9999
for i in range(2, 10001):
    if a[i]:
        for j in range(2 * i, 10001, i):
            a[j] = False

for _ in range(T):
    N = int(sys.stdin.readline())
    for i in range(N//2, 1, -1):
        if a[i] and a[N-i]:
            print(i, N-i)
            break


