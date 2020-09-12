import itertools

def solution(orders, course):
    answer = []
    order = []
    for i in orders:
        order.append("".join(sorted(i))) # sort

    li = []
    print(order)
    for n in course:
        result = []
        for i in order:
            coo = itertools.combinations(i, n)
            for l in coo:
                string = ""
                for k in l:
                    string += k
                count = 0
                for o in order:
                    c = 0
                    for of in o:
                        for k in string:
                            if k == of:
                                c += 1
                    if len(string) == c:
                        # print(string, o)
                        count += 1
                if count > 1:
                    result.append([string, count])
        result = sorted(result, key=lambda x: x[1], reverse=True)
        if result:
            MAX = result[0][1]
        for i in result:
            if i[1] == MAX:
                answer.append(i[0])
            else:
                break
    result = {}
    for i in answer:
        result[i] = True
    return sorted(list(result.keys()))
'''

    for n in course:
        com = itertools.combinations(li, n)
        cal = {}
        result = []

        for l in com: # string 목록
            string = ""
            for k in l:
                string += k
            count = 0
            for o in order:
                c = 0
                for of in o:
                    for k in string:
                        if k == of:
                            c += 1
                if len(string) == c:
                    #print(string, o)
                    count += 1
            #print(string, count)
            if count > 1:
                result.append([string, count])
        result = sorted(result, key = lambda x:x[1], reverse= True)
        #print(result)
        if result:
            MAX = result[0][1]
        #print(result)
        for i in result:
            if i[1] == MAX:
                answer.append(i[0])
            else:
                break
        #print(answer)
    print(answer)
    return sorted(answer)
'''

solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4])