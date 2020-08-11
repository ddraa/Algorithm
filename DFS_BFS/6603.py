from itertools import combinations
import sys, copy

while True:
    l = list(map(int, sys.stdin.readline().split()))
    if l[0] == 0:
        break
    s = l[1:]
    com = combinations(s,6)
    for i in com:
        for j in i:
            print(j, end= " ")
        print("")
    print("")