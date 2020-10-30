s1, s2 = [], []
for i in range(8):
    if i % 2 == 0:
        s1.append(list("WB" * 4))
        s2.append(list("BW" * 4))
    else:
        s2.append(list("WB" * 4))
        s1.append(list("BW" * 4))

MIN = float('inf')

matrix = []
x, y = map(int, input().split())
for _ in range(x):
    matrix.append(list(input()))

for i in range(x - 7):
    for j in range(y - 7):
        c1, c2 = 0, 0
        for a in range(8):
            for b in range(8):
                if matrix[i + a][j + b] != s1[a][b]:
                    c1 += 1
                if matrix[i + a][j + b] != s2[a][b]:
                    c2 += 1

        if MIN > min(c1, c2):
            MIN = min(c1, c2)
print(MIN)
