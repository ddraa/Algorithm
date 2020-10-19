import itertools, copy

def solution(user_id, banned_id):
    users_id = itertools.combinations(user_id, len(banned_id))
    temp = copy.deepcopy(banned_id)
    count = 0
    answer = []
    for users in users_id:
        use_per = itertools.permutations(users) # all permutation of users
        for users_list in use_per:
            for user in users_list:
                for ban in banned_id:
                    removed = False
                    if len(user) == len(ban):
                        Flag = True
                        for i in range(len(ban)):
                            if ban[i] != '*' and user[i] != ban[i]:
                                Flag = False
                        if Flag: # can mapping
                            removed = True
                            banned_id.remove(ban)
                    if removed:
                        break
            if not banned_id and users not in answer:
                answer.append(users)
                count += 1
                banned_id = copy.deepcopy(temp)
                break
            banned_id = copy.deepcopy(temp)
    return count

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "*rodo", "******", "******"]))