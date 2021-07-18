import sys

sys.setrecursionlimit(10 ** 7)


def divide(in_s, in_e, post_s, post_e):
    root = postorder[post_e]

    if in_s > in_e or post_s > post_e:
        return
    root_index = roots[root]
    l_nodes = root_index - in_s

    print(root, end=" ")
    divide(in_s, root_index - 1, post_s, post_s + l_nodes - 1)  # left subtree
    divide(root_index + 1, in_e, post_s + l_nodes, post_e - 1) # right subtree


N = int(sys.stdin.readline())
inorder = list(map(int, sys.stdin.readline().split()))
roots = [0] * (N + 1)
for i in range(N):
    roots[inorder[i]] = i

postorder = list(map(int, sys.stdin.readline().split()))
divide(0, N - 1, 0, N - 1)
