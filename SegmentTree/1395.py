import sys
input = sys.stdin.readline


def init(si, ei, node=1):
    if si == ei:
        tree[node] = arr[si]
        return tree[node]
    else:
        mid = (si + ei) // 2
        tree[node] = init(si, mid, node * 2) + init(mid + 1, ei, node*2 + 1)
        return tree[node]


def query(qli, qri, si, ei, node=1):
    update_lazy(si, ei, node)
    if qli > ei or qri < si:
        return 0
    if qli <= si and ei <= qri:
        return tree[node]

    mid = (si + ei) // 2
    return query(qli, qri, si, mid, node * 2) + query(qli, qri, mid + 1, ei, node*2 + 1)


def update_lazy(si, ei, node):
    if lazy[node] != 0:
        tree[node] = ei - si + 1 - tree[node]

        if si != ei:
            lazy[node*2] = not lazy[node*2]
            lazy[node*2 + 1] = not lazy[node*2 + 1]
        lazy[node] = 0


def update_range(qli, qri, v, si, ei, node=1):
    update_lazy(si, ei, node)
    if ei < qli or si > qri:
        return

    if qli <= si and ei <= qri:
        tree[node] = ei - si + 1 - tree[node]
        if si != ei:
            lazy[node*2] = not lazy[node*2]
            lazy[node*2 + 1] = not lazy[node*2 + 1]
        return

    mid = (si + ei) // 2
    update_range(qli, qri, v, si, mid, node * 2)
    update_range(qli, qri, v, mid + 1, ei, node*2 + 1)
    tree[node] = tree[node*2] + tree[node*2 + 1]


N, M = map(int, input().split())
tree = [0] * (4 * N)
lazy = [0] * (4 * N)
arr = [0] * N
init(0, N - 1)

for _ in range(M):
    o, s, t = map(int, input().split())
    s -= 1
    t -= 1
    if o == 0:
        update_range(s, t, 1, 0, N - 1)
    else:
        print(query(s, t, 0, N - 1))