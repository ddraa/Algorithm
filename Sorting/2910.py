import sys

n, c = map(int, sys.stdin.readline().split())
l = list(map(int, sys.stdin.readline().split()))
dic = {}
for i in l:
    if i not in dic:
        c = 0
        for j in l:
            if i == j:
                c += 1
        dic[i] = c
res = sorted(dic.items(), key=lambda x:x[1], reverse=True)
for d in res:
    for _ in range(d[1]):
        print(d[0], end=' ')