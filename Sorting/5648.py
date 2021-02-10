import sys

f = False
N = None
arr = []

while True:
    l = sys.stdin.readline().split()
    if l:
        if not f:
            N = int(l[0])
            f = True
            for i in range(1, len(l)):
                arr.append(int(l[i][::-1]))
        else:
            for i in range(len(l)):
                arr.append(int(l[i][::-1]))
        if len(arr) == N:
            break


for n in sorted(arr):
    print(n)