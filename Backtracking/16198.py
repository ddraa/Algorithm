import sys
sys.setrecursionlimit(10 ** 8)
MAX = float('-inf')

def DFS(n, s):
    global MAX, w
    if n == 3:
        if MAX < s + w[0] * w[2]: MAX = w[0] * w[2] + s
        return
    else:
        for i in range(1, len(w) - 1):
            t = w[i]
            s += w[i-1] * w[i+1]
            del w[i]
            DFS(n - 1, s)
            w.insert(i, t)
            s -= w[i-1] * w[i+1]

N = int(input())
w = list(map(int, input().split()))
DFS(N, 0)
print(MAX)