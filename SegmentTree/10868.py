import sys
input = sys.stdin.readline

def init(si, ei, node = 1):
    if si == ei:
        tree[node] = arr[si]
        return tree[node]
    else:
        mid = (si + ei) // 2
        tree[node] = min(init(si, mid, node * 2), init(mid + 1, ei, node*2 + 1))
        return tree[node]


def query(qli, qri, si, ei, node = 1):
    if qli > ei or qri < si:
        return 1e9 + 1
    if qli <= si and ei <= qri:
        return tree[node]

    mid = (si + ei) // 2
    return min(query(qli, qri, si, mid, node * 2), query(qli, qri, mid + 1, ei, node*2 + 1))


def update(index, v, si, ei, node = 1):
    if index < si or index > ei:
        return
    tree[node] += v
    if si != ei:
        mid = (si + ei) // 2
        update(index, v, si, mid, node * 2)
        update(index, v, mid + 1, ei, node*2 + 1)

arr = []
N, M = map(int, input().split())
tree = [0] * (4 * N)
for _ in range(N):
    arr.append(int(input()))
init(0, N - 1)
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    print(query(a, b, 0, N - 1))

