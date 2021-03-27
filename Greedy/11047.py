import sys

N, K = map(int, sys.stdin.readline().split())
coin = []
for index in range(N):
    coin.append(int(sys.stdin.readline()))
    if coin[index] <= K:
        i = index # check

c = 0
while i >= 0:
    q, r = divmod(K, coin[i])
    c += q
    K = r
    i -= 1
print(c)