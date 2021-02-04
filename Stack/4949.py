import sys

while True:
    s = sys.stdin.readline()[:-1]
    if s == '.':
        break

    stack = []
    for i in s:
        if i == '[' or i == '(':
            stack.append(i)
        elif i == ']':
            if not stack or stack.pop() != '[':
                print("no")
                break
        elif i == ')':
            if not stack or stack.pop() != '(':
                print("no")
                break
    else:
        if stack:
            print("no")
        else:
            print("yes")