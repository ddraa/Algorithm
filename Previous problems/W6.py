def solution(logs):
    answer = []
    people = {}
    for l in logs:
        t = l.split()
        ID, q, score = t[0], int(t[1]), int(t[2])
        if ID in people:
            for s in people[ID]:
                if s[0] == q: # exist
                    s[1] = score
                    break
            else:
                people[ID].append([q, score])

        else:
            people[ID] = list()
            people[ID].append([q, score])

    for p1 in people:
        for p2 in people:
            if p1!=p2:
                if len(people[p1]) == len(people[p2]) and len(people[p1]) >= 5:
                    c = 0
                    for a in people[p1]:
                        if a in people[p2]:
                            c += 1
                            continue
                    if c == len(people[p1]):
                        if p1 not in answer:
                            answer.append(p1)
                        if p2 not in answer:
                            answer.append(p2)
    if len(answer) == 0:
        return ["None"]
    else:
        answer.sort()
        return answer


print(solution(["1901 1 100", "1901 2 100", "1901 4 100", "1901 7 100", "1901 8 100", "1902 2 100", "1902 1 100", "1902 7 100", "1902 4 100", "1902 8 100", "1903 8 100", "1903 7 100", "1903 4 100", "1903 2 100", "1903 1 100", "2001 1 100", "2001 2 100", "2001 4 100", "2001 7 95", "2001 9 100", "2002 1 95", "2002 2 100", "2002 4 100", "2002 7 100", "2002 9 100"]	*200))