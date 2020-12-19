import sys
sx, sy = set(), set()
for _ in range(2):
    x, y = map(int, sys.stdin.readline().split())
    sx.add(x), sy.add(y)
x, y = map(int, sys.stdin.readline().split())
if x not in sx:
    rx = x
else:
    for k in sx:
        if k != x:
            rx = k
if y not in sy:
    ry = y
else:
    for k in sy:
        if k != y:
            ry = k
print(rx, ry)