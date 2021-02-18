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
                #arr.append(j - lp + 2)
                i = table[i]
                return True
            else:
                i += 1
    return False


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


string = []
n, k = map(int, sys.stdin.readline().split())
for _ in range(n):
    input()
    string.append(sys.stdin.readline().split())
sample = string[0]


for s in range(len(sample) - k + 1):
    pattern = sample[s:s + k]
    c = 0
    for ss in range(1, n):
        ans = KMP(pattern, string[ss])
        if not ans:
            ans = KMP(list(reversed(pattern)), string[ss])
            if not ans:
                break
            else:
                c += 1
        else:
            c += 1
    if c == n - 1:
        print("YES")
        exit(0)
print("NO")

