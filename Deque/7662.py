# 이중 우선순위 큐
import sys, bisect
from collections import deque

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    arr = deque() # 덱을 사용
    dic = {}

    for _ in range(n):
        op, num = sys.stdin.readline().split()
        num = int(num)
        if op == 'I':
            if num not in dic: # 중복을 체크하여 저장
                dic[num] = 1
                bisect.insort(arr, num) # 이분탐색 활용
            else:
                dic[num] += 1
        else:
            if not arr:
                continue
            if num == 1: #최댓값을 삭제
                dic[arr[-1]] -= 1 # 하나 -- 조절
                if dic[arr[-1]] == 0: # 수량 체크.. 더이상 없다면
                    del dic[arr[-1]] # 아예 삭제
                    arr.pop()

            else: # 최솟값을 삭제
                dic[arr[0]] -= 1
                if dic[arr[0]] == 0:
                    del dic[arr[0]]
                    arr.popleft()

    print(arr[-1], arr[0]) if arr else print("EMPTY")