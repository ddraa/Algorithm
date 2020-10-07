def solution(n):
    s = []
    l = []
    for i in range(n):
        t = []
        for j in range(i+1):
            t.append(0)
        s.append(t)
    sx,sy = 0, 0
    ex,ey = n-1, n-1
    c = 1
    while True:
        for i in s: # check
            if 0 in i:
                break
        else:
            break
        x = sx
        y = sy

        while x <= ex: # down
            s[x][y] = c
            c += 1
            x += 1

        x -= 1
        y += 1
        while y < ey: # right
            s[x][y] = c
            c += 1
            y += 1


        while x > sx:
            s[x][y] = c
            c += 1
            x -= 1
            y -= 1

        sx = x + 2
        sy = y + 1
        ex -= 1
        ey -= 2
    for i in s:
        for k in i:
            l.append(k)
    return l
