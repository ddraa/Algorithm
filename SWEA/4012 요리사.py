import itertools

T = int(input())
for _ in range(T):
    N = int(input())
    matrix = []
    sample = range(N)
    for _ in range(N):
        matrix.append(list(map(int, input().split())))
    case = itertools.combinations(sample, N//2)
    r = []

    for c in case: # each c 0 1 2
        s = 0
        ca = itertools.combinations(c, 2) # 0 1
        for k in ca:
            a, b = k
            s += matrix[a][b]
            s += matrix[b][a]
        li = []
        for al in sample:
            if al in c:
                continue
            else:
                li.append(al)
        ca = itertools.combinations(li, 2)
        s1 = 0
        for k in ca:
            a, b = k
            s1 += matrix[a][b]
            s1 += matrix[b][a]
        r.append(abs(s1-s))
    print(min(r))
