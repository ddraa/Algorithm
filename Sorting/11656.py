import sys

l = []
s = sys.stdin.readline().rstrip()
i = 0
while i < len(s):
    l.append(s[i:])
    i += 1
for k in sorted(l):
    print(k)