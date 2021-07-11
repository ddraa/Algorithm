import sys
input = sys.stdin.readline

def init(si, ei, node=1):
    if si == ei:
        tree[node] = si
    else:
        mid = (si + ei) // 2
        init(si, mid, node * 2)
        init(mid + 1, ei, node*2 + 1)

        if arr[tree[node * 2]] <= arr[tree[node * 2 + 1]]:
            tree[node] = tree[node * 2]
        else:
            tree[node] = tree[node * 2 + 1]


def query(qli, qri, si, ei, node=1):
    if qli > ei or qri < si:
        return N
    if qli <= si and ei <= qri:
        return tree[node]

    mid = (si + ei) // 2

    i1 = query(qli, qri, si, mid, node * 2)
    i2 = query(qli, qri, mid + 1, ei, node*2 + 1)

    return i1 if arr[i1] <= arr[i2] else i2


def update(index, v, si, ei, node=1):
    if index < si or index > ei:
        return

    if si == ei:
        arr[index] = v
    else:
        mid = (si + ei) // 2
        update(index, v, si, mid, node * 2)
        update(index, v, mid + 1, ei, node*2 + 1)

        if arr[tree[node*2]] <= arr[tree[node*2 + 1]]:
            tree[node] = tree[node*2]
        else:
            tree[node] = tree[node*2 + 1]


N = int(input())
tree = [0] * (4 * N)
arr = list(map(int, input().split()))
arr.append(1e9 + 1)
init(0, N - 1)
M = int(input())
for _ in range(M):
    n, a, b = map(int, input().split())
    a -= 1
    if n == 1:
        update(a, b, 0, N - 1)
    else:
        b -= 1
        print(query(a, b, 0, N - 1) + 1)
