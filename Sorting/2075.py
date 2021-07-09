import sys, heapq
# 19m

def solve():
    N = int(sys.stdin.readline())
    h = []
    for i in range(N):
        s = list(map(int, sys.stdin.readline().split()))
        for j in range(N):
            if len(h) < N:
                heapq.heappush(h, s[j])
            else:
                if h[0] < s[j]:
                    heapq.heappop(h)
                    heapq.heappush(h, s[j])
    print(heapq.heappop(h))
    return


if __name__ == '__main__':
    solve()
