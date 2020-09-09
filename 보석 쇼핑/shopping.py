from _collections import deque

def solution(gems):
    answer = []
    li = set(gems)
    length = len(gems)
    left = 1; right = length
    d = -1
    while left<=right:
        mid = (left + right) // 2
        temp = deque()
        t = {}
        c = 0
        for k in range(length): ### each case simulation
            temp.append(gems[k])
            if gems[k] in t:
                t[gems[k]] += 1
            else:
                t[gems[k]] = 1
            c += 1
            if c == mid:
                if len(li) != len(t):
                    delete = temp.popleft()
                    if t[delete] == 1:
                        del t[delete]
                    else:
                        t[delete] -= 1
                    c -= 1
                else: # OK
                    d = mid
                    right = mid-1
                    answer.append([k+1-d+1, k+1, d])
                    print(answer)
                    break
        else:
            left = mid + 1
    return answer[-1][:2]

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))