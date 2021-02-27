import sys
used = {chr(k + ord('a')) : 1 for k in range(26)}

def dfs(d, s):
    if d == L:
        jc = 0
        for ss in s:
            if ss in "aeiou":
              jc += 1
        if jc >= 1 and L - jc >= 2:
            print(s)
        return

    for al in alpa:
        if not s or (not used[al] and al > s[-1]):
            used[al] = 1
            dfs(d + 1, s + al)
            used[al] = 0


L, C = map(int, sys.stdin.readline().split())
alpa = sorted(sys.stdin.readline().split())
for a in alpa:
    used[a] = 0

dfs(0, "")