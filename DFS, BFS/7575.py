import sys

n, k = map(int, sys.stdin.readline().split())
arr = []
m = float('inf')
for _ in range(n):
    N = int(sys.stdin.readline())
    if m > N:
        m = N
    arr.append(list(map(int, sys.stdin.readline().split())))
succeed = False
for c in range(k,m+1): # c is #of check length not index
    i = 0
    last = m-c
    while c+i<=m:
        ok = 0
        state = arr[0][i:c+i]
        for j in range(1,n):
            l = 0
            while l <= last:
                #print(f'j = {j}일때 {state}와 {arr[j][l:c+l]}비교')
                if not(state[0] == arr[j][l] or state[0] == arr[j][l+c-1]):
                    l += 1
                    continue
                if state == arr[j][l:c+l] or state == list(reversed(arr[j][l:c+l])):
                    #print(f'j = {j}, state = {state}')
                    ok += 1
                    break
                l += 1
            if not ok:
                break
        if ok == n-1:
            print("YES")
            succeed = True
            break
        i += 1
    if succeed:
        break
if not succeed:
    print("NO")
