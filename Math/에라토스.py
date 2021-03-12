import sys
N = int(sys.stdin.readline())
a = [False, False] + [True] * (N - 1)
primes = []

for i in range(2, N + 1):
  if a[i]:
    primes.append(i)
    for j in range(i * i, N + 1, i): # 최적화
        a[j] = False