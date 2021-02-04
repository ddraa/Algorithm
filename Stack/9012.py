import sys

for _ in range(int(sys.stdin.readline())):
    s = sys.stdin.readline().rstrip()
    stack = []

    for i in s:
        if i == '(':
            stack.append(i)
        else:
            if stack:
                stack.pop()
            else:
                print("NO")
                break
    else:
        if stack:
            print("NO")
        else:
            print("YES")