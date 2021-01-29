import sys
from collections import deque

def sol():
    ops = sys.stdin.readline().strip()
    N = int(sys.stdin.readline())

    if N:
        l = deque(sys.stdin.readline().strip()[1:-1].split(','))
    else:
        _ = input()
        l = []

    rev = 0
    for op in ops:
        if op == 'R':
            rev += 1
        else:
            if not l:
                print("error")
                return
            if rev % 2 == 1:
                l.pop()
            else:
                l.popleft()

    if rev % 2 == 1:
        print(f'[{",".join(reversed(l))}]')
    else:
        print(f'[{",".join(l)}]')

for _ in range(int(sys.stdin.readline())):
    sol()