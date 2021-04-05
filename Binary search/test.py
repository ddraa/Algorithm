import sys

N, M, L = map(int, sys.stdin.readline().split())
road = list(map(int, sys.stdin.readline().split()))
road.append(0)
road.append(L)
road.sort()

N += 2
lo, hi = 1, L-1
while lo <= hi:
    d = (lo+hi)//2
    count = 0
    for index in range(1, N):
        dist = road[index] - road[index-1]
        count += (dist//d)
        if dist%d == 0:
            count -= 1

    if count > M:
        lo = d+1
    else:
        ans = d
        hi = d-1
print(ans)