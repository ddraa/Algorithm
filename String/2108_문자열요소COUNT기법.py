from collections import Counter

T = int(input())
a = []
for _ in range(T):
    a.append(int(input()))
a.sort()
c = Counter(a).most_common(2)

print(round(sum(a)/T))
print(a[T//2])
if len(c) == 1:
    print(c[0][0])
else:
    if c[0][1] == c[1][1]:
        print(c[1][0])
    else:
        print(c[0][0])
print(abs(a[-1]-a[0]))