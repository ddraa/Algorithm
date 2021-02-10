import sys
from collections import deque

N = int(sys.stdin.readline())
for _ in range(N):
    n, m = map(int, sys.stdin.readline().split())
    A = list(map(int ,sys.stdin.readline().split()))
    B = list(map(int ,sys.stdin.readline().split()))

    A = deque(sorted(A, reverse=True))
    B = deque(sorted(B, reverse=True))
    c = 0
    while A and B:
        if A and A[0] > B[0]:
            c += len(B)
            A.popleft()
        else:
            while B and A[0] <= B[0]:
                B.popleft()
    print(c)

