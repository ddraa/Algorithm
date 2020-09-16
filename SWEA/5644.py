
T = int(input())
for ll in range(1, T+1):
    matrix = [[[] for _ in range(10) ] for _ in range(10)]
    M, A = map(int, input().split())
    A_move = list(map(int, input().split()))
    B_move = list(map(int, input().split()))

    A_move.insert(0, 0)
    B_move.insert(0, 0) # init

    for k in range(1, A+1):
        x, y, c, p = map(int, input().split())
        x -= 1
        y -= 1

        upperx = y - c # upper bound
        uppery = x
        i = 1
        while upperx <= y: ## top
            s = uppery
            for l in range(i):
                if 0<= uppery + l <= 9 and 0<=upperx<=9:
                    matrix[upperx][uppery + l].append([k, p])
            upperx += 1
            uppery = s - 1
            i += 2


        lowerx = y + c # lower bound
        lowery = x
        i = 1
        while lowerx > y: ## bottom
            s = lowery
            for l in range(i):
                if 0 <= lowery + l <= 9 and 0<=lowerx<=9:
                    matrix[lowerx][lowery + l].append([k, p])
            lowerx -= 1
            lowery = s - 1
            i += 2

    TA = []
    ax , ay = 0, 0
    TB = []
    bx, by = 9, 9
    for a in A_move:
        if a == 1 : #up
            ax -= 1
        elif a == 2: #right
            ay += 1
        elif a == 3: # down
            ax += 1
        elif a == 4: # left
            ay -= 1
        TA.append(matrix[ax][ay])

    for b in B_move:
        if b == 1:  # up
            bx -= 1
        elif b == 2:  # right
            by += 1
        elif b == 3:  # down
            bx += 1
        elif b == 4:  # left
            by -= 1
        TB.append(matrix[bx][by])
    score = 0
    for ta, tb in zip(TA, TB):
        if len(ta) == 0 and len(tb) == 0:
            continue
        elif len(ta) == 0 and len(tb) != 0:
            tb = sorted(tb, key=lambda z: z[1], reverse=True)
            score += tb[0][1]
        elif len(ta) != 0 and len(tb) == 0:
            ta = sorted(ta, key=lambda z: z[1], reverse=True)
            score += ta[0][1]
        else:
            ta = sorted(ta, key=lambda z: z[1], reverse=True)
            tb = sorted(tb, key=lambda z: z[1], reverse=True)
            if ta[0][0] != tb[0][0]: # diffent
                score += ta[0][1]
                score += tb[0][1]
            else:
                M = ta[0][1]
                score += M
                temp = []
                for tt in ta:
                    if tt[1] != M:
                        temp.append(tt[1])
                for tt in tb:
                    if tt[1] != M:
                        temp.append(tt[1])
                if temp:
                    score += max(temp)
                else: # half sum
                    continue
    print(f'#{ll} {score}')
