import sys
s = sys.stdin.readline().rstrip()
stack = []
p = None
c = 0
for k in s:
    if k == '(':
        stack.append(k)
    else:
        if p == '(': # razer
            stack.pop()
            c += len(stack)
        else: # stick end
            stack.pop()
            c += 1
    p = k
print(c)

