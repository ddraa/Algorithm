import sys
input = sys.stdin.readline
mod = 1e9 + 7


def init(si, ei, node=1):
    if si == ei:
        tree[node] = arr[si]
        return tree[node]
    else:
        mid = (si + ei) // 2
        tree[node] = (init(si, mid, node * 2) + init(mid + 1, ei, node*2 + 1)) % mod
        return tree[node]


def query(qli, qri, si, ei, node=1):
    update_lazy(si, ei, node)
    if qli > ei or qri < si:
        return 0
    if qli <= si and ei <= qri:
        return tree[node]

    mid = (si + ei) // 2
    return query(qli, qri, si, mid, node * 2) ^ query(qli, qri, mid + 1, ei, node*2 + 1)


def update_lazy(si, ei, node):
    if lazy[1][node] == 0 and lazy[0][node] == 1:
        return
    if si != ei:
        for i in range(2*node, 2*node + 2):
            lazy[0][i] = lazy[0][node] * lazy[0][i] % mod
            lazy[1][i] = (lazy[0][node] * lazy[1][i] % mod + lazy[1][node]) % mod

    tree[node] = (lazy[0][node] * tree[node] % mod + lazy[1][node] * (ei - si + 1) % mod) % mod
    lazy[0][node] = 1
    lazy[1][node] = 0


def update_range(qli, qri, si, ei, _mul, _sum, node=1):
    update_lazy(si, ei, node)
    if ei < qli or si > qri:
        return

    if qli <= si and ei <= qri:
        lazy[0][node] = lazy[0][node] * _mul % mod
        lazy[1][node] = lazy[1][node] * _mul % mod
        lazy[1][node] = (lazy[1][node] + _sum) % mod
        update_lazy(si, ei, node)
        return

    mid = (si + ei) // 2
    update_range(qli, qri, si, mid, _mul, _sum, node * 2)
    update_range(qli, qri, mid + 1, ei, _mul, _sum, node * 2 + 1)
    tree[node] = tree[node*2] + tree[node*2 + 1]

N = int(input())
tree = [0] * (4 * N)
lazy = [[0] * (4 * N) for _ in range(2)]
print(lazy)
arr = list(map(int, input().split()))
init(0, N - 1)
M = int(input())
for _ in range(M):
    q = list(map(int, input().split()))
    if q[0] == 1:
        _, x, y, val = q
        x -= 1
        y -= 1
        update_range(x, y, 0, N - 1, 1, val)
    elif q[0] == 2:
        _, x, y, val = q
        x -= 1
        y -= 1
        update_range(x, y, 0, N - 1, val, 0)
    elif q[0] == 3:
        _, x, y, val = q
        x -= 1
        y -= 1
        update_range(x, y, 0, N - 1, 0, val)
    else:
        _, x, y = q
        x -= 1
        y -= 1
        print(query(x, y, 0, N - 1))












