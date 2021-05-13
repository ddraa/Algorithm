from heapq import *
import sys


def check(h):
    if not h:
        return False
    else:
        return True


def sol():
    dist, h = [], []
    cl, c = 0, 0

    N = int(sys.stdin.readline())
    for _ in range(N):
        a, b = map(int, sys.stdin.readline().split())
        dist.append((a, b))

    L, P = map(int, sys.stdin.readline().split())
    dist.sort()

    for p, w in dist:
        go = p - cl
        P -= go

        while P < 0:
            if not check(h):
                return -1
            P += -heappop(h)
            c += 1

        cl = p
        heappush(h, -w)

    P -= L - cl
    while P < 0:
        if not check(h):
            return -1
        P += -heappop(h)
        c += 1
    return c


print(sol())
