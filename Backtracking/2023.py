import sys
import math

def dfs(n, d):
    if d == N:
        print(n)
        return

    for k in range(10):
        nn = 10 * n + k

        for a in range(2, int(math.sqrt(nn)) + 1):
            if nn % a == 0:
                break
        else:
            dfs(nn, d + 1)

N = int(sys.stdin.readline())
for i in range(10):
    if i in [2, 3, 5, 7]:
        dfs(i, 1)