N = int(input())
l = input()
if "LL" in l:
    l = l.replace("LL", "S")
    print(len(l) + 1)
else:
    print(N)