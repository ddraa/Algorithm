N = int(input())

for i in range(10**7):
    if str(i).count('666') > 0:
        N -= 1
        if N == 0:
            print(i)
            break