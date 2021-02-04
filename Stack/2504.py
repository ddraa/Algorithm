import sys, re
s = sys.stdin.readline().rstrip()
stack, check = [], []
flag, p = True, None

for i in s: #check
    if i == '(' or i == '[':
        check.append(i)
    else:
        if check:
            k = check.pop()
            if not(k + i == "()" or k + i == "[]"):
                flag = False
        else:
            flag = False

if check or not flag:
    print(0)
else:
    for i in s:
        if i == '(' or i == '[':
            stack.append(i)
        else:
            if i == ')':
                if p == '(':
                    stack.pop()
                    stack.append(2)
                else:
                    t = 0
                    while stack[-1] != '(':
                        t += stack.pop()
                    stack.pop()
                    stack.append(2 * t)
            elif i == ']':
                if p == '[':
                    stack.pop()
                    stack.append(3)
                else:
                    t = 0
                    while stack[-1] != '[':
                        t += stack.pop()
                    stack.pop()
                    stack.append(3 * t)
        p = i
    print(sum(stack))