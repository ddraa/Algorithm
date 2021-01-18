from itertools import product

N, M = map(int, input().split())
s = set(map(int, input().split()))
sort = sorted(list(s))
for i in product(sort, repeat=M):
    print(*i)