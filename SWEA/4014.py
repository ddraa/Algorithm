

def checks(mat):
    global N, X
    count = 0

    ## row check
    for row in mat:
        check = row[0] # first unit
        i = 1
        while i < N:
            succeed = True
            if check != row[i] and abs(check - row[i]) == 1:
                k = i
                c = 0
                temp = row[i]
                OK = False
                while k < k+X and k < N :
                    if row[k] == temp:
                        c += 1
                        if c == X:
                            OK = True
                            last_index = k
                            break
                        else:
                            succeed = False
                    k += 1
                if OK:
                    i = last_index
                    check = row[i]
                    continue
            elif check == row[i]:
                pass
            else: # 높이 1 차이 넘게 나면
                succeed = False
            i += 1
            if not succeed:
                break
        if succeed:
            print(row)
            count += 1




    ## column check


    return count
T = int(input())

for ll in range(1, T+1):
    N, X = map(int, input().split())
    matrix = []
    for _ in range(N):
        matrix.append(list(map(int, input().split())))

    answer = checks(matrix)
    print(answer)