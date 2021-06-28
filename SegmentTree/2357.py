import sys
input = sys.stdin.readline


def init_min(si, ei, node=1):
    if si == ei:
        treem[node] = arr[si]
        return treem[node]
    else:
        mid = (si + ei) // 2
        treem[node] = min(init_min(si, mid, node * 2), init_min(mid + 1, ei, node * 2 + 1))
        return treem[node]


def query_min(qli, qri, si, ei, node=1):
    if qli > ei or qri < si:
        return 1e9 + 1
    if qli <= si and ei <= qri:
        return treem[node]

    mid = (si + ei) // 2
    return min(query_min(qli, qri, si, mid, node * 2), query_min(qli, qri, mid + 1, ei, node * 2 + 1))


def init_max(si, ei, node=1):
    if si == ei:
        treeM[node] = arr[si]
        return treeM[node]
    else:
        mid = (si + ei) // 2
        treeM[node] = max(init_max(si, mid, node * 2), init_max(mid + 1, ei, node * 2 + 1))
        return treeM[node]


def query_max(qli, qri, si, ei, node=1):
    if qli > ei or qri < si:
        return 0
    if qli <= si and ei <= qri:
        return treeM[node]

    mid = (si + ei) // 2
    return max(query_max(qli, qri, si, mid, node * 2), query_max(qli, qri, mid + 1, ei, node * 2 + 1))


arr = []
N, M = map(int, input().split())
treem = [0] * (4 * N)
treeM = [0] * (4 * N)

for _ in range(N):
    arr.append(int(input()))
init_min(0, N - 1)
init_max(0, N - 1)
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    print(query_min(a, b, 0, N - 1), query_max(a, b, 0, N - 1))
