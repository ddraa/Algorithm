class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class NodeMgmt:
    def __init__(self, data):
        self.head = Node(data)

    def add(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)


    def delete(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            deleted = self.head
            self.head = self.head.next
            del deleted
        else:
            node = self.head
            while node.next:
                if node.next.data == data:
                    deleted = node.next
                    node.next = node.next.next
                    del deleted
                    return
                node = node.next


    def search(self, data):
        node = self.head
        while node:
            if node.data == data:
                return node
            node = node.next
        return node


    def print(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next


linkedlist = NodeMgmt(0)
for i in range(1, 10):
    linkedlist.add(i)
linkedlist.delete(4)