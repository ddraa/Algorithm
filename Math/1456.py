import sys
s, n = map(int, sys.stdin.readline().split())
MAX = 10 ** 7

a = [False, False] + [True] * (MAX - 1)
primes = []

for i in range(2, MAX + 1):
  if a[i]:
    primes.append(i)
    for j in range(2 * i, MAX + 1, i):
        a[j] = False

c = 0
for p in primes:
    i = 2
    while p ** i <= n:
        if s <= p ** i <= n:
            c += 1
        i += 1
print(c)