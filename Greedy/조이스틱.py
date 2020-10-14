
al = {}
for i in range(26):
    al[chr(ord('A') + i)] = i

def solution(name):
    answer = 0
    temp = ['A'] * len(name)
    k = 0
    while True:
        if name[k] != temp[k]:
            answer += min(al[name[k]], 26 - al[name[k]])
            temp[k] = name[k] # set
        else:
            END = False
            l = k - 1 if k >= 1 else len(name) - 1
            lc = 1

            r = (k + 1) % len(name)
            rc = 1

            while name[l] == temp[l]:
                l = l - 1 if l >= 1 else len(name) - 1
                lc += 1
                if lc > len(name):
                    return answer
            while name[r] == temp[r]:
                r = (r + 1) % len(name)
                rc += 1

            k = r if lc > rc else l
            answer += min(lc, rc)


print(solution("AAAA"))