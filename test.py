answer = []
dx = {}
dy = {}
v = [[1, 4], [3, 4], [3, 10]]
for i in v:
    if i[0] in dx: dx[i[0]] += 1
    else: dx[i[0]] = 1
    if i[1] in dy: dy[i[1]] += 1
    else: dy[i[1]] = 1
for kx, ky in zip(dx.keys(), dy.keys()):
    print(kx, ky)
    if dx[kx] == 1:
        x = kx
    if dy[ky] == 1:
        y = ky

print(dx)
print(dy)
print(x, y)