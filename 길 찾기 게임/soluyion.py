import sys
sys.setrecursionlimit(10**6)

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class NodeMgmt:
    def __init__(self, head):
        self.head = head

    def insert(self, value):
        self.current_node = self.head
        while True:
            if value < self.current_node.value:
                if self.current_node.left != None:
                    self.current_node = self.current_node.left
                else:
                    self.current_node.left = Node(value)
                    break
            else:
                if self.current_node.right != None:
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = Node(value)
                    break

def pre(root):
    if not root:
        return
    temp.append(dic[root.value])
    pre(root.left)
    pre(root.right)


def post(root):
    if not root:
        return
    post(root.left)
    post(root.right)
    temp.append(dic[root.value])


answer = []
temp = []
info = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]
dic = {}
for i in range(len(info)):
    dic[info[i][0]] = i+1
info = sorted(info,key =lambda x : x[1], reverse=True)


head = Node(info[0][0])
btree = NodeMgmt(head)
for i in range(1,len(info)):
    btree.insert(info[i][0])

pre(btree.head)
answer.append(temp)
temp = []
post(btree.head)
answer.append(temp)
print(answer)