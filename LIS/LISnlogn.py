import sys
import bisect

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
dp = []

for n in arr:
    k = bisect.bisect_left(dp, n)
    if len(dp) == k:
        dp.append(n)
    else:
        dp[k] = n
print(len(dp))
