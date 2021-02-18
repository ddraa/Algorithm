import sys

def table(P):
    lp = len(P)
    Table = [0] * lp
    i = 0
    for j in range(1, lp):
        while i > 0 and P[i] != P[j]:
            i = Table[i - 1]

        if P[i] == P[j]:
            i += 1
            Table[j] = i
    return Table

input()
MAX, CMAX = 0, 0
t = sys.stdin.readline().split()
for k in range(len(t)):
    sub = t[k:]
    ans = table(sub)
    if MAX < ans[-1]:
        MAX = ans[-1]
        CMAX = k
print(MAX, CMAX) if MAX != 0 else print(-1)
