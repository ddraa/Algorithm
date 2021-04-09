import sys

while True:
    try:
        N = int(sys.stdin.readline())
    except:
        break
    dp = [1, 1, 3]

    for i in range(3, N + 1):
        dp.append(dp[i-1] + 2 * dp[i-2])
    print(dp[N])