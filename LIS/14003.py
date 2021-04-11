import sys
import bisect

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
dp, index, res = [], [], []
dic = {}

for n in arr:
    k = bisect.bisect_left(dp, n)
    if len(dp) == k:
        dp.append(n)
    else:
        dp[k] = n
    index.append(k)

count = max(index)
i = index.index(count)

while i >= 0: # 역추적 과정
    if count == index[i]:
        res.append(arr[i])
        count -= 1
    i -= 1

print(len(res))
print(*reversed(res))
