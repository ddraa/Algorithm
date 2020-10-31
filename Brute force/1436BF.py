a = int(input())
b = int(input())
flag = True
s = 0
for i in range(a, b+1):
    c = 0
    for j in range(1, i):
        if i % j == 0:
            c += 1
            if c > 1:
                break
    else:
        if flag:
            M = i
            flag = False
        s += i
if not flag:
    print(s)
    print(M)
else:
    print(-1)