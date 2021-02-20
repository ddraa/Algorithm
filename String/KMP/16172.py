import sys

def KMP(P,T):
    arr = []
    lt = len(T)
    lp = len(P)
    table = LIS(P)
    i = 0
    for j in range(lt):
        while i > 0 and P[i] != T[j]:
            i = table[i - 1]
        if P[i] == T[j]:
            if i == lp - 1:
                arr.append(j - lp + 2)
                i = table[i]
            else:
                i += 1
    return arr


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


temp = sys.stdin.readline().rstrip()
p = sys.stdin.readline().rstrip()
t = ""
for a in temp:
    if not a.isdigit():
        t += a

ans = KMP(p, t)
print(1) if ans else print(0)
