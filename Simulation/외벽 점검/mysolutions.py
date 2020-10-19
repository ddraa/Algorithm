from _collections import deque
from itertools import permutations
import copy


def alloc(li, d):
    s = li[0] # start
    while li[0] <= s+d:
        li.pop(0)
        if not li:
            return

def check(n, weak, dist):
    N = len(weak)
    for _ in range(N): # start order ..
        dist_list = permutations(dist, len(dist)) # caution !!! re-declaration
        li = []
        for i in range(1,N):
            li.append(weak[i])
        li.append(weak[0]+n)

        save = copy.deepcopy(li)
        for d in dist_list: # d is [4,3]
            for friend in d:
                alloc(li, friend)
                if not li:
                    return True
            li = copy.deepcopy(save)
        weak = copy.deepcopy(save)
    return False

def solution(n, weak, dist):
    dist.sort()
    l = []
    temp = copy.deepcopy(weak)
    for _ in range(len(dist)): # add to l ( list of dist )

        l.append(dist.pop())
        c = len(l)
        s = check(n, weak, l)

        if s:
            return c
        weak = copy.deepcopy(temp)
    if s:
        return 1
    else:
        return -1

print(solution(12,[1, 5, 6, 10]	,[1, 2, 3, 4]))
