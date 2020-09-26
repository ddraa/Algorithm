N = int(input())
count = 0
for i in range(1, N+1):
    if i < 10:
        count += 1
        continue

    l = len(str(i)) - 1
    k = 0
    d = int(str(i)[k]) - int(str(i)[k+1])
    while k < l:
        if d != int(str(i)[k]) - int(str(i)[k+1]):
            break
        k += 1
    if k == l: # pass
        count += 1
print(count)