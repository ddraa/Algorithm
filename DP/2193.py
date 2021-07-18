import sys

N = int(sys.stdin.readline())
pinary = [0, 1]

for n in range(2, N + 1):
    pinary.append(pinary[n - 1] + pinary[n - 2])

print(pinary[-1])