i = 1
while True:
    l, p, v = map(int, input().split())
    if l == 0 and p == 0 and v == 0:
        break

    q, r = divmod(v, p)
    r = r if r < l else l
    print(f'Case {i}: {q * l + r}')
    i += 1