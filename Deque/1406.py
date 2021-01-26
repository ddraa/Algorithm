from collections import deque
import sys

left = deque(sys.stdin.readline().strip())
M = int(sys.stdin.readline())
right = deque()
for _ in range(M):
    op = sys.stdin.readline().split()
    if op[0] == 'P':
        left.append(op[1])
    elif op[0] == 'L':
        if left:
            right.appendleft(left.pop())
    elif op[0] == 'D':
        if right:
            left.append(right.popleft())
    else:
        if left:
            left.pop()
print("".join(left) + "".join(right))