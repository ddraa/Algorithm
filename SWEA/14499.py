N, M, x, y, K = map(int, input().split())
MAP = []
dice = [[0]*3 for _ in range(4)]

for _ in range(N):
    MAP.append(list(map(int, input().split())))

order = list(map(int, input().split()))
cur_x, cur_y = x, y
dice_x, dice_y = 1, 1 # toward bottom 4X3
for d in order:
    Check = True
    if d == 4: # South, dice upper
        cur_x += 1
        if 0 <= cur_x <= N - 1 and 0 <= cur_y <= M - 1:
            temp = dice[0][1]
            k = 0
            while k<=2:
                dice[k][1] = dice[k+1][1]
                k += 1
            dice[k][1] = temp
        else:
            Check = False
            cur_x -= 1

    elif d == 3: # North
        cur_x -= 1
        if 0 <= cur_x <= N - 1 and 0 <= cur_y <= M - 1:
            temp = dice[3][1]
            k = 3
            while k >= 1:
                dice[k][1] = dice[k - 1][1]
                k -= 1
            dice[k][1] = temp
        else:
            Check = False
            cur_x += 1

    elif d == 2: # west
        cur_y -= 1
        if 0 <= cur_x <= N - 1 and 0 <= cur_y <= M - 1:

            temp = dice[3][1]
            dice[3][1] = dice[1][2]
            dice[1][2] = dice[1][1]
            dice[1][1] = dice[1][0]
            dice[1][0] = temp

        else:
            Check = False
            cur_y += 1
    else:
        cur_y += 1
        if 0 <= cur_x <= N - 1 and 0 <= cur_y <= M - 1:
            temp = dice[3][1]
            dice[3][1] = dice[1][0]
            dice[1][0] = dice[1][1]
            dice[1][1] = dice[1][2]
            dice[1][2] = temp
        else:
            Check = False
            cur_y -= 1

    if Check:
        if MAP[cur_x][cur_y] != 0:
            dice[dice_x][dice_y] = MAP[cur_x][cur_y]
            MAP[cur_x][cur_y] = 0
        else:
            MAP[cur_x][cur_y] = dice[dice_x][dice_y]

        print(dice[(dice_x+2)%4][1])


