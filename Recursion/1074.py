def solve(n, row, col):
    if n == 0:
        return 0
    half = 2 ** (n - 1)

    if row < half and col < half:
        return solve(n - 1, row, col)
    if row < half <= col:
        return half * half + solve(n - 1, row, col - half)
    if col < half <= row:
        return 2 * half * half + solve(n - 1, row - half, col)
    else:
        return 3 * half * half + solve(n - 1, row - half, col - half)


N, r, c = map(int, input().split())
print(solve(N, r, c))
