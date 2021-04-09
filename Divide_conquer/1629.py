def solve(A, B, m):
    if B == 1: # base condition
        return A % m

    tres = solve(A, B//2, m)
    res = tres * tres % m
    if B % 2 == 0:
        return res
    else:
        return res * A % m

a, b, c = map(int, input().split())
print(solve(a, b, c))