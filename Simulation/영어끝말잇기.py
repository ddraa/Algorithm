def solution(n, words):
    dic = {words[0] : True}

    for i in range(len(words) - 1):
        if words[i][-1] == words[i+1][0] and words[i+1] not in dic:
            dic[words[i+1]] = True
        else:
            return [(i + 1) % n + 1, (i + 1) // n + 1]
    else:
        return [0, 0]

print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))