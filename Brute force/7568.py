N = int(input())
l = []
for _ in range(N):
    l.append(list(map(int, input().split())))
for i in l:
    c = 0
    for j in l:
        if i[0] < j[0] and i[1] < j[1]:
            c += 1
    print(c + 1, end= " ")