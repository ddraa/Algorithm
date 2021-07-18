def gcd(a, b):
    if b == 0:
        return a

    return gcd(b, a % b)

def solution(x, y):
    # visited = [[False for _ in range(y)] for _ in range(x)]
    # N = x * y
    # ox, oy = x, y
    # x, y = 0, 0 # start
    # c = 0
    # while True:
    #     if not visited[x][y]:
    #         visited[x][y] = True
    #         c += 1
    #         if c == N:
    #             return True
    #         x = (x + 1) % ox
    #         y = (y + 1) % oy
    #     else:
    #         return False

    if x % 2 == 0 and y % 2 == 0:
        return False
    else:
        return True

    #
    # if gcd(x, y) != 1:
    #     return False
    # else:
    #     return True

print(solution(2, 5))