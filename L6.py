def solution(companies, applicants):
    answer = []

    rejected = []
    com = {}
    ap = {}
    for i in companies:
        t = i.split()
        com[t[0]] = []
        com[t[0]].append(t[1])
        com[t[0]].append(t[2])
        com[t[0]].append([])

    for i in applicants:
        t = i.split()
        ap[t[0]] = []
        ap[t[0]].append(t[1])
        ap[t[0]].append(t[2])



    while True:
        k = 0
        for people in ap:
            com[ap[people][0][k]][2].append(people) # k 순위의 회사 지원

        for c in com:
            while int(com[c][1])< len(com[c][2]): # 지원자가 더 많으면
                rank = com[c][0]
                for i in range(len(rank)-1, -1, -1): # 역순으로
                    if rank[i] in com[c][2]:
                        com[c][2].remove(rank[i]) # 삭제

        break

    print(ap)

    print(com)

    return answer

solution(["A fabdec 2", "B cebdfa 2", "C ecfadb 2"]	,["a BAC 1", "b BAC 3", "c BCA 2", "d ABC 3", "e BCA 3", "f ABC 2"]	)