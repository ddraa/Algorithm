import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

dpf = [1] * N
dpb = [1] * N
res = [1] * N

for i in range(N):
    for j in range(i):
        if arr[i] > arr[j]:
            dpf[i] = max(dpf[i], dpf[j] + 1)

for i in range(N - 2, -1, -1):
    for j in range(N - 1, i, -1):
        if arr[i] > arr[j]:
            dpb[i] = max(dpb[i], dpb[j] + 1)

for i in range(N):
    res[i] = dpf[i] + dpb[i] - 1

print(max(res))