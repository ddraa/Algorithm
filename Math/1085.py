import sys
x, y, w, h = map(int, sys.stdin.readline().split())
print(min(min(x, abs(w-x)), min(y, abs(h-y))))