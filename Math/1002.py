import math
T = int(input())

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    R, r = max(r2, r1), min(r2, r1)
    d = math.sqrt(abs(x2 - x1) ** 2 + abs(y2 - y1) ** 2)
    if R == r and x1 == x2 and y1 == y2: print(-1)
    else:
        if d > R + r:print(0)
        elif d == R + r:print(1)
        elif d > R - r:print(2)
        elif d == R - r:print(1)
        else:print(0)
