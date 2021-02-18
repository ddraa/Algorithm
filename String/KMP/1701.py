import sys

def LIS(P):
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

t = sys.stdin.readline().rstrip()
MAX = 0
for a in range(len(t)):
    sub = t[a:]
    ans = max(LIS(sub))
    if MAX < ans:
        MAX = ans
print(MAX)

