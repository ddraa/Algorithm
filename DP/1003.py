a, b = [1, 0], [0, 1]
l = [a, b] #init

for _ in range(40):
    na = [a[0]+b[0], a[1]+b[1]]
    l.append(na)
    b, a = na, b

T = int(input())
for _ in range(T):
    print(*l[int(input())])
