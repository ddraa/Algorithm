import sys
N = int(sys.stdin.readline())
l = []
for _ in range(N):
    n, a, b, c = sys.stdin.readline().split()
    l.append((n, int(a), int(b), int(c)))
l.sort(key=lambda x:(-x[1], x[2], -x[3], x[0]))
for p in l:
    print(p[0])