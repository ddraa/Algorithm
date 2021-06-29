import sys
input = sys.stdin.readline

def init(si, ei, node=1):
    if si == ei:
        tree[node] = arr[si]
        return tree[node]
    else:
        mid = (si + ei) // 2
        tree[node] = (init(si, mid, node * 2) * init(mid + 1, ei, node*2 + 1)) % 1000000007
        return tree[node]


def query(qli, qri, si, ei, node=1):
    if qli > ei or qri < si:
        return 1
    if qli <= si and ei <= qri:
        return tree[node]

    mid = (si + ei) // 2
    return (query(qli, qri, si, mid, node * 2) * query(qli, qri, mid + 1, ei, node*2 + 1)) % 1000000007


def update(index, o, new, si, ei, node=1):
    if index < si or index > ei:
        return

    if si == ei:
        tree[node] = new
        return

    mid = (si + ei) // 2
    update(index, o, new, si, mid, node * 2)
    update(index, o, new, mid + 1, ei, node*2 + 1)
    tree[node] = (tree[node*2] * tree[node*2 + 1]) % 1000000007


N, M, K = map(int, input().split())
tree = [0] * (4 * N)
arr = []
for _ in range(N):
    arr.append(int(input()))

init(0, N - 1)
for _ in range(M + K):
    a, b, c = map(int, input().split())
    b -= 1
    if a == 1:
        origin = arr[b]
        arr[b] = c
        after = c
        update(b, origin, after, 0, N - 1)
    else:
        c -= 1
        print(query(b, c, 0, N - 1))