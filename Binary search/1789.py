import sys
S = int(sys.stdin.readline())

left = 1
right = S
while left <= right:
    m = (left + right) // 2
    if m*(m+1)/2 > S :
        right = m - 1
    else:
        left = m + 1
print(left - 1)