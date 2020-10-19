from _collections import deque


T = int(input())
for ll in range(1, T+1):
    K = int(input())
    c = []
    for _ in range(4):
        c.append(deque(map(int, input().split())))
    for _ in range(K):
        x, direct = map(int, input().split())
        d_save = direct
        x_save = x - 1
        x -= 1

        dic = {x:direct}
        while x < 3: # ---->
            direct = 1 if direct == -1 else -1
            if c[x][2] != c[x+1][6]:
                dic[x+1] = direct
            else:
                break
            x += 1
        x = x_save # cur val index
        direct = d_save
        while x > 0: # <------
            direct = 1 if direct == -1 else -1
            if c[x][6] != c[x-1][2]:
                dic[x-1] = direct
            else:
                break
            x -= 1
        for key in dic:
            if dic[key] == 1:
                c[key].appendleft(c[key].pop())
            else:
                c[key].append(c[key].popleft())
    score = 0
    for i in range(4):
        if c[i][0] == 1:
            score += 2**i
    print(f'#{ll} {score}')