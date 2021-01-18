MAX = float('-inf')
def DFS(d, c):
    global MAX
    if d == N:
        if c > MAX: MAX = c
        return

    if egg[d][0] <= 0 or c >= N - 1:
        DFS(d + 1, c)
    else:
        for i in range(N):
            if d != i and egg[i][0] > 0:
                egg[d][0] -= egg[i][1]
                egg[i][0] -= egg[d][1]
                if egg[d][0] <= 0: c += 1
                if egg[i][0] <= 0: c += 1
                DFS(d + 1, c)
                if egg[d][0] <= 0: c -= 1
                if egg[i][0] <= 0: c -= 1
                egg[d][0] += egg[i][1]
                egg[i][0] += egg[d][1]


N = int(input())
egg = []
for _ in range(N):
    egg.append(list(map(int, input().split())))

DFS(0, 0)
print(MAX)