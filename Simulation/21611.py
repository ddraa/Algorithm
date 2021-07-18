import sys

N, M = map(int, sys.stdin.readline().split())
ds, dq, board = [], [], []
one, two, three = 0, 0, 0

for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))
for _ in range(M):
    ds.append(list(map(int, sys.stdin.readline().split())))

sx, sy = N // 2, N // 2
step = 2

while sx != 0 or sy != 0: # listing
    sy -= 1
    dq.append(board[sx][sy])
    for _ in range(step - 1):
        sx += 1
        dq.append(board[sx][sy])

    for _ in range(step):
        sy += 1
        dq.append(board[sx][sy])

    for _ in range(step):
        sx -= 1
        dq.append(board[sx][sy])

    for _ in range(step):
        sy -= 1
        dq.append(board[sx][sy])
    step += 2

for i in range(M): # blizard
    d, s = ds[i]
    if d == 1:
        jump = None
        cur = 6
        for k in range(s):
            del dq[cur]
            cur -= 1
            if jump is None:
                jump = 15
            else:
                jump += 8
            cur += jump

            if cur >= len(dq):
                break

    elif d == 2:
        jump = None
        cur = 2
        for k in range(s):
            del dq[cur]
            cur -= 1
            if jump is None:
                jump = 11
            else:
                jump += 8
            cur += jump

            if cur >= len(dq):
                break

    elif d == 3:
        jump = None
        cur = 0
        for k in range(s):
            del dq[cur]
            cur -= 1
            if jump is None:
                jump = 9
            else:
                jump += 8
            cur += jump

            if cur >= len(dq):
                break

    else:
        jump = None
        cur = 4
        for k in range(s):
            del dq[cur]
            cur -= 1
            if jump is None:
                jump = 13
            else:
                jump += 8
            cur += jump

            if cur >= len(dq):
                break

    while True: # boom
        removed = []
        f = False
        before = dq[0]
        c = 1
        for d in range(1, len(dq)):
            if dq[d] == before:
                c += 1
            else:
                if c >= 4:
                    f = True
                    if before == 1:
                        one += c
                    elif before == 2:
                        two += c
                    else:
                        three += c

                    for l in range(c):
                        removed.append(d - c + l)
                c = 1
                before = dq[d]

        while removed:
            r = removed.pop()
            del dq[r]

        if not f:
            break

    new = []
    before = dq[0]
    c = 1
    for d in range(1, len(dq)):
        if before == dq[d]:
            c += 1
        else:
            new.append(c)
            new.append(before)
            if len(new) == N * N - 1:
                break

            c = 1
            before = dq[d]

    for _ in range(c): # left
        new.append(before)
    dq = new

print(1 * one + 2 * two + 3 * three)
