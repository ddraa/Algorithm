import sys
a = [False,False] + [True]*(2 * 123456 - 1)
for i in range(2, 123456 * 2 + 1):
    if a[i]:
        for j in range(2 * i, 123456 * 2 + 1, i):
            a[j] = False
while True:
    N = int(sys.stdin.readline())
    if N == 0:
        break
    c = 0
    for i in range(N + 1, 2 * N + 1):
        if a[i]:
            c += 1
    print(c)

