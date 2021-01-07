import sys, copy
sys.setrecursionlimit(10 ** 8)
MAX = float('-inf')

def DFS(n, s):
    global MAX, w
    if n == 3:
        if MAX < s + w[0] * w[2]: MAX = w[0] * w[2] + s
        return
    else:
        co = copy.deepcopy(w) # cur stage save
        for i in range(1, len(w) - 1):
            temp = w[i-1] * w[i+1]
            s += temp
            del w[i]
            DFS(n - 1, s)
            w = copy.deepcopy(co) # restore
            s -= temp

N = int(input())
w = list(map(int, input().split()))
DFS(N, 0)
print(MAX)