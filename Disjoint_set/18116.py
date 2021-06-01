import sys
input = sys.stdin.readline
MAX = 10 ** 6 + 1

def find(u):
    if u != p[u]:
        p[u] = find(p[u])
    return p[u]


def union(u, v):
    r1, r2 = find(u), find(v)
    p[r2] = r1


N = int(input())
group = [1 for _ in range(MAX)]
p = [i for i in range(MAX)]
for _ in range(N):
    l = input().split()
    if l[0] == 'I':
        a, b = int(l[1]), int(l[2])
        if find(a) != find(b):
            s = group[find(a)] + group[find(b)]
            union(a, b)
            group[find(a)] = s

    else:
        k = int(l[1])
        print(group[find(k)])

