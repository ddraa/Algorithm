import itertools

def solution(user_id, banned_id):
    dic = {}
    li, answer = [], []
    count = 0
    for k in banned_id:
        if k not in dic:
            dic[k] = []
    for user in user_id:
        for ban in banned_id:
            if len(user) == len(ban):
                Flag = True
                for i in range(len(ban)):
                    if ban[i] != '*' and ban[i] != user[i]: # not appropriate sample
                        Flag = False
                        break
                if Flag and user not in dic[ban]:
                    dic[ban].append(user)

    for k in banned_id:
        li.append(dic[k])
    it = itertools.product(*li)

    for i in it:
        if len(set(i)) == len(i):
            k = sorted(i)
            if k not in answer:
                answer.append(k)
                count += 1
    return count


print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "*rodo", "******", "******"]))