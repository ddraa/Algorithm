import itertools

MIN = float('inf')
N = int(input())
matrix = []

people = []
for i in range(N):
    people.append(i) # set people

for _ in range(N):
    matrix.append(list(map(int, input().split())))

com = itertools.combinations(people, N//2) #
for c in com: #
    Ascore = 0
    c_com = itertools.combinations(c, 2) #
    for p in c_com:
        x, y = p
        Ascore += matrix[x][y]
        Ascore += matrix[y][x]

    B_p = [] # set B
    Bscore = 0
    for p in people:
        if p not in c:
            B_p.append(p)
    b_com = itertools.combinations(B_p, 2)
    for p in b_com:
        x, y = p
        Bscore += matrix[x][y]
        Bscore += matrix[y][x]

    if abs(Ascore-Bscore) < MIN:
        MIN = abs(Ascore-Bscore)
print(MIN)