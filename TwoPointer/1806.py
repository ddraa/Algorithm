import sys

N, res = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

l, r = 0, 0
s = arr[0]
MIN = N + 1

while True:
    if s >= res:
        while s >= res:
            s -= arr[l]
            l += 1

            if s >= res:
                if MIN > r - l + 1:
                    MIN = r - l + 1
    else:
        r += 1
        if r == N:
            break

        s += arr[r]
        if s >= res:
            if r - l + 1 < MIN:
                MIN = r - l + 1

print(MIN) if MIN != N + 1 else print(0)