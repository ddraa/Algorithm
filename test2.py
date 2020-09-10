import itertools
import copy

def solution(a):
    answer = -1
    M = len(a)# 4
    N = len(a[0]) # 3
    b = [[0]*N for _ in range(M)]
    hang = [0 for _ in range(M)]
    for i in range(M):
        hang[i] = i

    yul = []
    for i in range(N):
        c = 0
        for j in range(M):
            if a[j][i] == 1:
                c += 1
        yul.append([i,c])
    b_case = []
    for i in yul:
        sample = itertools.combinations(hang,i[1])
        ss = []
        for s in sample:
            t = []
            for a in s:
                t.append([a,i[0]])
            ss.append(t)
        b_case.append(ss)

    pro = []
    for i in b_case:
        pro.append(i)

    duct = itertools.product(*pro)

    rc = 0
    temp = copy.deepcopy(b)
    for i in duct:
        for j in i:
            for k in j:
                x, y = k
                b[x][y] = 1
        for ax in b:
            c1 = ax.count(1)
            if c1%2!=0: # 1의 개수 짝수
                break
        else:
            rc += 1

        b = copy.deepcopy(temp)



    return rc%(10**7+19)


solution([[0,1,0],[1,1,1],[1,1,0],[0,1,1]])