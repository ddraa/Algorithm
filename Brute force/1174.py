from itertools import combinations
l = []
N = int(input())
for n in range(1, 11):
    for k in combinations(range(10), n):
        st = ""
        for i in range(n - 1, -1, -1):
            st += str(k[i])
        l.append(int(st))
l.sort()
try:
    print(l[N-1])
except:
    print(-1)
