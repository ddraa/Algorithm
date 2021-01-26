import sys
from collections import deque

N = int(sys.stdin.readline())
for _ in range(N):
    queue = deque(sys.stdin.readline().strip())

    left, right = deque() ,deque()
    while queue:
        k = queue.popleft()

        if k == '<':
            if left:
                right.appendleft(left.pop())
        elif k == '>':
            if right:
                left.append(right.popleft())
        elif k == '-':
            if left:
                left.pop()
        else:
            left.append(k)

    print("".join(left) + "".join(right))


