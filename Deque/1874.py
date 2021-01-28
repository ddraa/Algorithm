import sys
import heapq
N = int(sys.stdin.readline())
arr = [i for i in range(N, 0, -1)]
stack, ans = [], []

def sol():
    for _ in range(N):
        n = int(sys.stdin.readline())

        while not stack or stack[-1] != n:
            if not arr:
                print("NO")
                return
            stack.append(arr.pop())
            ans.append("+")
        stack.pop()
        ans.append("-")
    for a in ans:
        print(a)
sol()
