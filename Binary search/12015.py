import sys

N = int(sys.stdin.readline())
vector = []
arr = list(map(int, sys.stdin.readline().split()))
vector.append(arr[0]) #init
for i in range(1, N):
    if arr[i] > vector[-1]:
        vector.append(arr[i])
    else:
        l = 0; r = len(vector)-1
        while l<=r:
            m = (l + r) // 2
            if vector[m] >= arr[i]:
                r = m - 1
            else:
                l = m + 1
        vector[l] = arr[i]
print(len(vector))