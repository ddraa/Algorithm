l = input()
a, b = 0, 0
i = 0
while i < len(l):
    if l[i] == '1':
        a += 1
        while i < len(l) and l[i] == '1':
            i += 1
    elif l[i] == '0':
        b += 1
        while i < len(l) and l[i] == '0':
            i += 1
print(min(a,b))
