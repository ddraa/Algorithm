N = int(input())
l = []
for _ in range(N):
    l.append(int(input()))
c = 0
for i in range(len(l) - 1, 0, -1):
    if l[i - 1] >= l[i]:
        c += l[i - 1] - l[i] + 1
        l[i - 1] = l[i] - 1
print(c)
