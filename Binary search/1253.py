import sys, copy

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

rarr = copy.deepcopy(arr)
c = 0
for t in range(N):
    dest = arr[t]
    tarr = arr[:t] + arr[t + 1:]
    tarr.sort()
    l, r = 0, N - 2
    while l < r < N - 1:
        s = tarr[l] + tarr[r]

        if dest > s:
            l += 1
        elif dest < s:
            r -= 1
        else:
            c += 1
            break
    arr = copy.deepcopy(rarr)
print(c)
