import sys

N, k = map(int, sys.stdin.readline().split())
k -= 1
i = 1
li = []
Len = None

while i * i <= N:
    if N % i == 0:
        li.append(i)
    if i * i == N: # 제곱수
        Len = len(li) * 2 - 1
    i += 1

if Len is None:
    Len = len(li) * 2
if Len - 1 < k:
    print(0)
else:
    if Len % 2 == 0: # 제곱 ㄴㄴ 수
        if Len // 2 <= k: # k 인덱스에 들어갈 수를 찾아라
            print(N // li[Len - 1 - k])
        else:
            print(li[k])
    else:
        if k == Len // 2:
            print(li[k])
        elif k > Len // 2:
            print(N // li[Len - 1 - k])
        else:
            print(li[k])