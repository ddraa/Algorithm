import sys

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

for _ in range(m):
    arr.sort()
    arr[0] = arr[0] + arr[1]
    arr[1] = arr[0]
print(sum(arr))