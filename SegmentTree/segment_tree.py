import sys
input = sys.stdin.readline

def init(si, ei, node = 1):
    if si == ei:
        tree[node] = arr[si]
        return tree[node]
    else:
        mid = (si + ei) // 2
        tree[node] = init(si, mid, node * 2) + init(mid + 1, ei, node*2 + 1)
        return tree[node]


def query(qli, qri, si, ei, node = 1):
    if qli > ei or qri < si:
        return 0
    if qli <= si and ei <= qri:
        return tree[node]

    mid = (si + ei) // 2
    return query(qli, qri, si, mid, node * 2) + query(qli, qri, mid + 1, ei, node*2 + 1)


def update(index, v, si, ei, node = 1):
    if index < si or index > ei:
        return
    tree[node] += v
    if si != ei:
        mid = (si + ei) // 2
        update(index, v, si, mid, node * 2)
        update(index, v, mid + 1, ei, node*2 + 1)


N, M, K = map(int, input().split())
tree = [0] * (4 * N)
arr = []
for i in range(N):
    arr.append(int(input()))

init(0, N - 1, 1)
for _ in range(M + K):
    a, b, c = map(int, input().split())
    b -= 1
    if a == 1:
        val = c - arr[b]
        arr[b] = c
        update(b, val, 0, N - 1)
    else:
        c -= 1
        print(query(b, c, 0, N - 1))