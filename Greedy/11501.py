import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    price = list(map(int, sys.stdin.readline().split()))

    MAX = price[N - 1]
    profit = 0
    i = N - 2

    while i >= 0:
        if MAX <= price[i]:
            MAX = price[i]
        else:
            profit += MAX - price[i]
        i -= 1
    print(profit)