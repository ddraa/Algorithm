def fi(N):
    if N == 1:
        return 1
    elif N == 0:
        return 0
    else:
        return fi(N-1) + fi(N-2)


N = int(input())
print(fi(N))