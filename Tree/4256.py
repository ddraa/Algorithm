import sys


def divide(Pre, In):
    if len(Pre) == 0:
        return

    root = Pre[0]
    root_index = In.index(root)
    left, right = In[:root_index], In[root_index + 1:]

    divide(Pre[1:1 + len(left)], left)  # left subtree
    divide(Pre[1 + len(left):], right)  # right subtree
    res.append(root)


T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())

    preorder = list(map(int, sys.stdin.readline().split()))
    inorder = list(map(int, sys.stdin.readline().split()))
    res = []
    divide(preorder, inorder)
    print(*res)
