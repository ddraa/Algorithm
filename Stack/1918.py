import sys
input = sys.stdin.readline
res = ""
s = input().strip()
stack = []
for a in s:
    if a.isalpha():
        res += a
    else:
        if a == '(':
            stack.append(a)
        elif a == '*' or a == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                res += stack.pop()
            stack.append(a)
        elif a == '+' or a == '-':
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.append(a)
        else:
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.pop()

while stack:
    res += stack.pop()
print(res)