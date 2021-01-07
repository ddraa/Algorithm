from itertools import permutations
X = input()
MIN = 10**6
pers = permutations(X, len(X))
for per in pers:
    num = ""
    for p in per:
        num += p
    num = int(num)
    if MIN > num > int(X):
        MIN = num
print(MIN) if MIN != 10**6 else print(0)