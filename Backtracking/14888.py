N = int(input())
digit = list(map(int, input().split()))
ops = list(map(int, input().split()))
MIN, MAX = float('inf'), float('-inf')

def cal(op, a, b):
    if op == 0: return a + b
    elif op == 1: return a - b
    elif op == 2: return a * b
    else:
        if a * b >= 0:
            return a // b
        else:
            if a < 0: return -(abs(a) // b)
            else: return -(a // abs(b))


def DFS(i, s):
    global MAX, MIN
    if i == N:
        if s > MAX:MAX = s
        if s < MIN:MIN = s
        return
    else:
        for k in range(4):
            if ops[k] > 0:
                ops[k] -= 1
                DFS(i + 1, cal(k, s, digit[i]))
                ops[k] += 1

DFS(1, digit[0])
print(MAX)
print(MIN)