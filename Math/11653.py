N = int(input())
#
# a = [False,False] + [True]*(N - 1)
# for i in range(2, N + 1):
#     if a[i]:
#         for j in range(2 * i, N + 1, i):
#             a[j] = False
i = 2
while N >= 2:
    if N % i == 0:
        print(i)
        N = N // i
        continue
    i += 1

