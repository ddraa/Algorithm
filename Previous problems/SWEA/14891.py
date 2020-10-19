from _collections import deque

chain = []
for _ in range(4):
    chain.append(deque(map(int, input())))

k = int(input())
for _ in range(k):
    n, clock = map(int, input().split())
    n -= 1 # index

    ## right check
    t = n + 1
    rot_direct = -1 if clock == 1 else 1
    rotate = [[n, clock]] # idx, direct
    while t <= 3:
        if chain[t-1][2] != chain[t][6]:
            rotate.append([t, rot_direct])
            rot_direct = -1 if rot_direct == 1 else 1
        else:
            break
        t += 1


    ## left check
    t = n - 1
    rot_direct = -1 if clock == 1 else 1
    while t >= 0:
        if chain[t][2] != chain[t+1][6]:
            rotate.append([t, rot_direct])
            rot_direct = -1 if rot_direct == 1 else 1
        else:
            break
        t -= 1

    for r in rotate:
        i, d = r
        if d == 1: # clock
            chain[i].appendleft(chain[i].pop())
        else:
            chain[i].append(chain[i].popleft())

s = 0
k = 0
for n in chain:
    if n[0] == 1:
        s = s + 2**k
    k += 1
print(s)