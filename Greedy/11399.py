import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
s, res = 0, 0
for i in arr:
    s += i
    res += s
print(res)