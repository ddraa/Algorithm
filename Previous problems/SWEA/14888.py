

def get(op, val, cur):
    if op == 0: # +
        return cur + val
    elif op == 1:
        return cur - val
    elif op == 2:
        return cur * val
    else:
        return int(cur / val)

def cal(i, re):
    global MAX, MIN
    if i == N:
        if re >= MAX:
            MAX = re
        if re <= MIN:
            MIN = re
        return

    for k in range(4):
        if oper[k] > 0: # can use ?
            oper[k] -= 1
            cal(i+1, get(k, number[i], re))
            oper[k] += 1


MAX = float('-inf')
MIN = float('inf')

N = int(input())
number = list(map(int, input().split()))
oper = list(map(int, input().split())) # oper -> +, -, *, /

cal(1, number[0])
print(MAX)
print(MIN)