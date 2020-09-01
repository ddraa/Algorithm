import copy

def solution(stones, k):
    temp = copy.deepcopy(stones)
    left = 1
    right = 2*10**8
    while left <= right:

        M = (left + right) // 2
        for i in range(len(stones)): # each case simulation
            if stones[i] <= M:
                stones[i] = 0
            else:
                stones[i] -= M
        d = 0
        for i in range(len(stones)): # checking
            if stones[i] == 0:
                d += 1
                if d == k:
                    right = M - 1
                    break
            else:
                d = 0
        else: # if not break ..
            left = M + 1
        stones = copy.deepcopy(temp)
    return left # '조건에 부합하는' 가장 마지막 원소
print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))