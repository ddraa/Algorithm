

def solution(n, delivery):
    answer = ''
    num = ['?' for _ in range(n + 1)]
    l = sorted(delivery, key = lambda x:x[2], reverse=True)
    for k in l:
        if k[2] == 1:
            num[k[0]] = 'O'
            num[k[1]] = 'O'
        else:
            if num[k[0]] == 'O':
                num[k[1]] = 'X'
            elif num[k[1]] == 'O':
                num[k[0]] = 'X'
            else:
                if num[k[0]] == 'X':
                    if num[k[1]] == 'O':
                        num[k[1]] = '?'
                elif num[k[1]] == 'X':
                    if num[k[0]] == 'O':
                        num[k[0]] = '?'
    for i in range(1, len(num)):
        answer += num[i]

    return answer

solution(7, [[5,6,0],[1,3,1],[1,5,0],[7,6,0],[3,7,1],[2,5,0]]	)