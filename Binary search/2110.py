import sys

N, C = map(int, sys.stdin.readline().split())
l = []
for _ in range(N):
    l.append(int(sys.stdin.readline()))
l.sort()

left = 1
right = l[N-1]-l[0]
def get_router(distance):
    count = 1
    cur = l[0] # installed
    for i in range(1, N):
        if cur + distance <= l[i]: # can install
            count += 1
            cur = l[i]
    return count
while left<=right:
    m = (left+right) // 2 #distance

    if get_router(m)>=C:
        left = m + 1
    else:
        right = m - 1
print(left-1)