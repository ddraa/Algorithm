N = int(input())
c = 0
vertical = [False] * N
ucros = [False] * (2 * N - 1)
dcros = [False] * (2 * N - 1)

def check(x, y):
    if not (vertical[y] or ucros[x + y] or dcros[x - y + N - 1]):
        return True
    return False

def DFS(d):
    global c
    if d == N:
        c += 1
        return
    else:
        for y in range(N):
            if check(d, y):
                vertical[y] = ucros[d + y] = dcros[d - y + N - 1] = True
                DFS(d + 1)
                vertical[y] = ucros[d + y] = dcros[d - y + N - 1] = False

DFS(0) # start
print(c)