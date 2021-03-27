import sys

String = sys.stdin.readline().rstrip()
t = ""
res = 0
sign = None
for s in String:
    if s.isdigit():
        t += s
    else:
        if sign is None:
            res += int(t)
        else:
            res -= int(t)
        t = ""

        if s == '-':
            sign = True

if sign is not None:
    res -= int(t)
else:
    res += int(t)
print(res)