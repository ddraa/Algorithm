import sys

def dfs(s):
    global leaf
    if not tree[s]:
        leaf += 1
    else:
        for ch in tree[s]:
            dfs(ch)

N = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))
removed = int(sys.stdin.readline())

tree = {i : list() for i in range(N)}
root = li.index(-1)
for child, parent in enumerate(li):
    if parent != -1:
        tree[parent].append(child)


leaf = 0
if removed != root:
    tree[li[removed]].remove(removed)
    dfs(root)
print(leaf)