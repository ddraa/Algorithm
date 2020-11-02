N, L = map(int, input().split())
p = list(map(int, input().split()))
p.sort()
c = 0
i = 1
s = p[0] - 0.5
while i < len(p):
    if L < p[i] - s + 0.5:
        c += 1
        s = p[i] - 0.5
    i += 1
print(c + 1)