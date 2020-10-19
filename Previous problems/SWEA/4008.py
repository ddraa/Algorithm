def dfs(i, result):
    global N, MAX, MIN
    if i == N:
        if result >= MAX:
            MAX = result
        if result <= MIN:
            MIN = result
        return

    for k in range(4): # + - * /
        if oper[k] > 0:
            oper[k] -= 1
            if k == 0: # +
                n_result = result + number[i] #### caution ! result += number[i] error..
            elif k == 1: # -
                n_result = result - number[i]
            elif k == 2:
                n_result = result * number[i]
            else:
                n_result = int(result / number[i])

            dfs(i+1, n_result)
            oper[k] += 1


T = int(input())


for ll in range(1, T+1):
    temp = []
    MAX = float('-inf')  # init
    MIN = float('inf')
    N = int(input())
    oper = list(map(int, input().split()))
    number = list(map(int, input().split()))
    dfs(1, number[0])
    print(f'#{ll} {abs(MAX-MIN)}')

