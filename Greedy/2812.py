N, k = map(int, input().split())
num = input()
res = [num[0]]
for i in range(N - 1):
    if num[i] < num[i + 1]:
        while res and res[-1] < num[i + 1] and k > 0:
            res.pop()
            k -= 1
    res.append(num[i + 1])
for _ in range(k):
    res.pop()
print(int("".join(res)))
