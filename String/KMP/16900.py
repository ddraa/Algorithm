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

t, k = sys.stdin.readline().split()
k = int(k)
ans = table(t)
print(k * len(t) - (k-1) * ans[-1])