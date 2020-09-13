from _collections import deque

def solution(ball, order):
    answer = []
    temp = []
    ball = deque(ball)
    for i in order:
        #print(i, ball)
        if i == ball[0]:
            ball.popleft()
            answer.append(i)

            t = 0
            L = len(temp)
            for _ in range(L):
                t = 0
                while t < len(temp):
                    if temp[t] == ball[0]:
                        ball.popleft()
                        answer.append(temp[t])
                        del temp[t]
                        t -= 1
                    elif temp[t] == ball[-1]:
                        ball.pop()
                        answer.append(temp[t])
                        del temp[t]
                        t -= 1
                    t += 1


        elif i == ball[-1]: # 24
            ball.pop()
            answer.append(i)


            t = 0
            L = len(temp)
            for _ in range(L):
                t = 0
                while t < len(temp):
                    if temp[t] == ball[0]:
                        ball.popleft()
                        answer.append(temp[t])
                        del temp[t]
                        t -= 1
                    elif temp[t] == ball[-1]:
                        ball.pop()
                        answer.append(temp[t])
                        del temp[t]
                        t -= 1
                    t += 1
        else:
            temp.append(i)
        #print(temp)
    print(answer)

    return answer

solution([11, 2, 9, 13, 24]	,[9, 2, 13, 24, 11]	)