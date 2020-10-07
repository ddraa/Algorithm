N = int(input())

n = 0
while True:
    if N == n + sum(map(int, str(n))):
        print(n)
        break
    n += 1
    if n == N:
        print(0)
        break