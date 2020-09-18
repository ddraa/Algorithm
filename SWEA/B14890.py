def check(mat):
    global count
    for road in mat: ## make horizontal
        build = [0 for _ in range(N)]
        i = 1
        temp = road[0]
        succeed = True
        while i < N:
            if temp != road[i]: #
                if road[i] > temp and road[i] - temp == 1: # upper
                    k = i - 1
                    c = 0
                    time = 0
                    while time < L and 0 <= k: # only during L..
                        if road[k] == temp and not build[k]:
                            build[k] = 1
                            c += 1
                        k -= 1
                        time += 1
                    if c == L:
                        temp = road[i] # adjust
                        pass
                    else:
                        succeed = False
                        break
                elif temp > road[i] and temp - road[i] == 1: # lower
                    k = i
                    c = 0
                    time = 0
                    while time < L and k < N:
                        if road[k] == road[i] and not build[k]:
                            build[k] = 1
                            c += 1
                        time += 1
                        k += 1
                    if c == L:
                        temp = road[i]
                        pass
                    else:
                        succeed = False
                        break
                else:
                    succeed = False
                    break
            i += 1
        if succeed:
            count += 1


N, L = map(int, input().split())
matrix, vertical = [], []

count = 0
for _ in range(N):
    matrix.append(list(map(int, input().split())))

for j in range(N): ## make vertical matrix
    t = []
    for i in range(N):
        t.append(matrix[i][j])
    vertical.append(t)

check(matrix)
check(vertical)
print(count)