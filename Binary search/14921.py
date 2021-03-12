import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

MIN = float('inf')
l, r = 0, N - 1

while l < r:
    dist = arr[r] + arr[l]
    if abs(dist) < MIN:
        MIN = abs(dist)
        al, ar = l, r

    if dist > 0:
        r -= 1
    else:
        l += 1
print(arr[al] + arr[ar])