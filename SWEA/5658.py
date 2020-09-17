from _collections import deque

def Tohex(n):
    return int(n, 16)

T = int(input())
for ll in range(1, T+1):
    N, K = map(int ,input().split())
    number = deque(input())
    length = N // 4
    li = set()

    for _ in range(length): # during length..  rotation
        t = []
        i = 0
        temp = ""
        while i < N:
            if len(temp) < length:
                temp += number[i]
            else:
                t.append(temp)
                temp = f'{number[i]}'
            i += 1
        t.append(temp) # last
        for num in t:
            li.add(Tohex(num))
        number.appendleft(number.pop()) # rotation
    result = sorted(list(li), reverse=True)
    print(f'#{ll} {result[K-1]}')


