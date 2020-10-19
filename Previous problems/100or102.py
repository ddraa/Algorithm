def index (l, r, score, people):
    while l <= r:
        m = (l + r) // 2
        if people[m][4] >= score:
            r = m - 1
        else:
            l = m + 1
    return l - 1

def solution(info, query):
    answer = []
    people = []
    for i in info:
        t = i.split()
        t[4] = int(t[4])
        people.append(t)
    #for i in people:
        #print(i)
    people = sorted(people, key = lambda x:x[4])
    #for i in people:
        #print(i)
    queue = []
    for q in query:
        #print(q)
        count = 0

        t = q.split()

        score = int(t[-1])

        left = 0
        right = len(info) - 1
        idx = index(left, right, score, people)
        while idx >=0 and people[idx][4] >= score:
            idx -= 1
        if idx < 0 :
            idx = 0
        for k in range(idx, len(people)): # K 번째 people에 대하
            OK = True
            for i in range(4):
                if t[i*2][0] != '-' and t[i*2][0] != people[k][i][0]:
                    break
            else:
                if t[-1] <= people[k][4]:
                    count += 1
        #print(count)
        answer.append(count)



    return answer

solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
         ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"])