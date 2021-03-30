import sys

N = int(sys.stdin.readline())
minus, plus = [], []
for _ in range(N):
    k = int(sys.stdin.readline())
    if k > 0:
        plus.append(k)
    else:
        minus.append(k)

plus.sort()
minus.sort(reverse=True)
res = 0
while len(minus) > 1:
    a = minus.pop()
    b = minus.pop()
    res += a * b

while len(plus) > 1:
    a = plus.pop()
    b = plus.pop()
    res += max(a * b, a + b)

while minus:
    res += minus.pop()
while plus:
    res += plus.pop()
print(res)
