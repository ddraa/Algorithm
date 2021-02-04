import sys
k = 1
while True:
    s = sys.stdin.readline().rstrip()
    if s.startswith('-'):
        break
    r, c = 0, 0
    stack = []
    for i in s:
        if i == "{":
            stack.append(i)
        else:
            if stack:
                stack.pop()
            else:
                r += 1

    l = len(stack)
    if l % 2 == 0 and r % 2 == 0:
        c = l // 2 + r // 2
    else:
        c = sum(divmod(l, 2)) + sum(divmod(r, 2))
    print(f'{k}. {c}')
    k += 1
