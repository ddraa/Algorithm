import sys
input = sys.stdin.readline
MAX = 200_000 + 1


def find(u):
    if u != p[u]:
        p[u] = find(p[u])
    return p[u]


def union(u, v):
    r1, r2 = find(u), find(v)
    p[r2] = r1
    count[r1] += count[r2]


T = int(input())
for _ in range(T):
    n = int(input())
    p = [i for i in range(MAX)]
    count = [1 for _ in range(MAX)]
    seq = 0
    key = {}

    for _ in range(n):
        a, b = input().split()
        if a not in key:
            key[a] = seq
            seq += 1
        if b not in key:
            key[b] = seq
            seq += 1
        A, B = key[a], key[b]

        if find(A) != find(B):
            union(A, B)

        root = find(B)
        print(count[root])
