import itertools

T = int(input())
for ll in range(1, T+1):
    N = int(input())
    matrix = []
    sample = range(N)
    for _ in range(N):
        matrix.append(list(map(int, input().split())))
    case = itertools.combinations(sample, N//2)
    r = []

    t = 1
    j = N
    for k in range(N//2): # nPr
        t *= j
        j -= 1
    j = N // 2
    tt = 1
    for k in range(N//2):
        tt *= j
        j -= 1
    length = t//tt / 2
    count = 0

    for c in case: # each c 0 1 2
        if count > length:
            break
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
        count += 1
    print(f'#{ll} {min(r)}')
