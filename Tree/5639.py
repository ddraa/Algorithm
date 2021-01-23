import sys
sys.setrecursionlimit(10**9)

class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)

        if self.root is None:
            self.root = new_node
            return

        current = self.root

        while True:
            parent = current
            if data < current.data:
                current = current.left
                if current is None:
                    parent.left = new_node
                    break
            else:
                current = current.right
                if current is None:
                    parent.right = new_node
                    break

    def post(self):
        def _post(node):
            if node is not None:
                _post(node.left)
                _post(node.right)
                print(node.data)
        _post(self.root)


l = []
while True:
    try:
        l.append(int(sys.stdin.readline()))
    except:
        break

bst = BinarySearchTree()
for x in l:
    bst.insert(x)

bst.post()