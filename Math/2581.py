import sys
M = int(sys.stdin.readline())
N = int(sys.stdin.readline())

s, MIN = 0, float('inf')
for i in range(M, N+1):
	if i == 1:
		continue
	c = 0
	for j in range(2, i+1):
		if i % j == 0:
			c += 1
		if c > 1:
			break
	else:
		s += i
		if MIN > i:
			MIN = i
if s == 0:
	print(-1)
else:
	print(s)
	print(MIN)