import sys, bisect
from collections import deque
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    arr = deque()
    dic = {}

    for _ in range(n):
        op, num = sys.stdin.readline().split()
        num = int(num)
        if op == 'I':
            if num not in dic:
                dic[num] = 1
                bisect.insort(arr, num)
            else:
                dic[num] += 1
        else:
            if not arr:
                continue
            if num == 1:
                dic[arr[-1]] -= 1
                if dic[arr[-1]] == 0:
                    del dic[arr[-1]]
                    arr.pop()

            else:
                dic[arr[0]] -= 1
                if dic[arr[0]] == 0:
                    del dic[arr[0]]
                    arr.popleft()

    print(arr[-1], arr[0]) if arr else print("EMPTY")