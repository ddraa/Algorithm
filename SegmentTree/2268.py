import sys
input = sys.stdin.readline

def init(si, ei, node=1):
    if si == ei:
        tree[node] = arr[si]
    else:
        mid = (si + ei) // 2
        init(si, mid, node * 2)
        init(mid + 1, ei, node*2 + 1)
        tree[node] = tree[node*2] + tree[node*2 + 1]


def query(qli, qri, si, ei, node=1):
    if qli > ei or qri < si:
        return 0
    if qli <= si and ei <= qri:
        return tree[node]

    mid = (si + ei) // 2
    return query(qli, qri, si, mid, node * 2) + query(qli, qri, mid + 1, ei, node*2 + 1)


def update(index, v, si, ei, node=1):
    if index < si or index > ei:
        return

    if si == ei:
        tree[node] = v
    else:
        mid = (si + ei) // 2
        if index <= mid:
            update(index, v, si, mid, node * 2)
        else:
            update(index, v, mid + 1, ei, node*2 + 1)
        tree[node] = tree[node*2] + tree[node*2 + 1]


N, Q = map(int, input().split())
tree = [0] * (4 * N)
arr = [0] * N
for _ in range(Q):
    n, i, j = map(int, input().split())
    if n == 0:
        if i > j:
            i, j = j, i
        print(query(i - 1, j - 1, 0, N - 1))
    else:
        update(i - 1, j, 0, N - 1)