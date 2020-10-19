def is_OK(answer, what):
    for x, y, what in answer:
        if what == 0: # bar
           if not (y == 0 or [x, y-1, 0] in answer or [x-1, y, 1] in answer or [x, y, 1] in answer):
               return False
        else: # bo
            if not([x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or ([x - 1, y, 1] in answer and [x + 1, y, 1] in answer)):
                return False
    return True
def solution(n, build_frame):
    answer = []

    for i in build_frame:
        x, y, what, op = i
        if op : # build
            answer.append([x, y, what])
            if not is_OK(answer, what):
                answer.remove([x, y, what])
        else: # del
            answer.remove([x, y, what])
            if not is_OK(answer, what):
                answer.append([x, y, what])

    return sorted(answer, key = lambda k :(k[0], k[1], k[2]))

print(solution(5,[[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))