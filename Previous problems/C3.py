


def solution(k, score):
    dic = {}
    for i in range(len(score)-1):
        dif = score[i] - score[i+1]
        if dif in dic:
            dic[dif].update([i, i+1])
        else:
            dic[dif] = set()
            dic[dif].update([i, i+1])
    c = 0
    t = set()
    print(dic)

    for d in dic:
        #print(d)
        if len(dic[d]) >= k+2:
            #print(dic[d])

            t |=  dic[d]
    #print(t)

    print(len(score) - len(t))
print(solution(2, [1300000000,700000000,668239490,618239490,568239490,568239486,518239486,157658638,157658634,100000000,100]			))