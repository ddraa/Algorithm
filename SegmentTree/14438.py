import sys
input = sys.stdin.readline
mxL = 1e9 + 1


def init(si, ei, node=1):
    if si == ei:
        tree[node] = arr[si]
        return tree[node]
    else:
        mid = (si + ei) // 2
        tree[node] = min(init(si, mid, node * 2), init(mid + 1, ei, node*2 + 1))
        return tree[node]


def query(qli, qri, si, ei, node=1):
    if qli > ei or qri < si:
        return mxL
    if qli <= si and ei <= qri:
        return tree[node]

    mid = (si + ei) // 2
    return min(query(qli, qri, si, mid, node * 2), query(qli, qri, mid + 1, ei, node*2 + 1))


def update(index, v, si, ei, node=1):
    if index < si or index > ei:
        return

    if si != ei:
        mid = (si + ei) // 2
        update(index, v, si, mid, node * 2)
        update(index, v, mid + 1, ei, node*2 + 1)
    else:
        tree[node] += v
        return

    tree[node] = min(tree[node * 2], tree[node*2 + 1])

N = int(input())
tree = [0] * (4 * N)
arr = list(map(int, input().split()))
init(0, N - 1)
M = int(input())
for _ in range(M):
    a, b, c = map(int, input().split())
    b -= 1
    if a == 1:
        val = c - arr[b]
        arr[b] = c
        update(b, val, 0, N - 1)
    else:
        c -= 1
        print(query(b, c, 0, N - 1))