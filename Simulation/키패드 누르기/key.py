def solution(numbers, hand):
    answer = ''

    keypad = [[1,2,3],[4,5,6],[7,8,9],['*',0,'#']]
    lp = [3,0]
    rp = [3,2]

    for i in numbers:
        if i in [1,4,7]:
            if i == 1:
                lp = [0,0]
            elif i == 4:
                lp = [1,0]
            else:
                lp = [2,0]
            answer += "L"
        elif i in [3,6,9]:
            if i == 3:
                rp = [0,2]
            elif i == 6:
                rp = [1,2]
            else:
                rp = [2,2]
            answer += "R"
        else:
            for k in range(len(keypad)):
                if keypad[k][1] == i:
                    ip = [k,1]
                    break
            dl = abs(k-lp[0]) + abs(1-lp[1])
            dr = abs(k-rp[0]) + abs(1-rp[1])
            if dl == dr :
                if hand == "right":
                    answer += 'R'

                else:
                    answer += 'L'
            else:
                if dl > dr:
                    answer += 'R'
                else:
                    answer += 'L'
            if answer[-1] == 'R':
                rp = [k,1]
            else:
                lp = [k,1]

    return answer

solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right")