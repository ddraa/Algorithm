import sys

n, dest = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

l, r = 0, 0
c = 0

s = arr[l]
while r < n:
    if dest == s:
        c += 1

        if l == r:
            l += 1
            r += 1
            if r < n:
                s = arr[l]
        else:
            s -= arr[l]
            l += 1
            r += 1
            if r < n:
                s += arr[r]
    elif dest < s:
        s -= arr[l]
        l += 1
    else:
        r += 1
        if r < n:
            s += arr[r]

print(c)
