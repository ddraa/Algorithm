n, m = map(int, input().split())

def cal(N, div):
    c = 0
    while N != 0:
        N //= div
        c += N
    return c

k = min(cal(n, 5) - cal(n - m, 5) - cal(m, 5), cal(n, 2) - cal(m, 2) - cal(n - m, 2))
print(k) if k > 0 else(print(0))