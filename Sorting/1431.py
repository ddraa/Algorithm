import sys

N = int(sys.stdin.readline())
arr = [sys.stdin.readline().rstrip() for _ in range(N)]
for i in range(N):
    s = 0
    for k in arr[i]:
        if k.isdigit():
            s += int(k)
    arr[i] = [arr[i], s]
arr.sort(key=lambda x: (len(x[0]), x[1], x[0]))
for a in arr:
    print(a[0])