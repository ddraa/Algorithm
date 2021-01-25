class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

class NodeMgmt:
    def __init__(self, data):
        self.head = Node(data)
        self.tail = self.head

    def insert(self, data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            node = self.head
            while node.next:
                node = node.next
            new_node = Node(data)

            node.next = new_node
            new_node.prev = node
            self.tail = new_node


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


    def search_from_head(self, data):
        if self.head is None:
            return False

        node = self.head
        while node:
            if node.data == data:
                return node
            node = node.next
        return False


    def search_from_tail(self, data):
        if self.tail is None:
            return False

        node = self.tail
        while node:
            if node.data == data:
                return node
            node = node.prev
        return False

    def insert_before(self, data, before_data):
        if self.head is None:
            self.head = Node(data)
            return True
        else:
            node = self.tail
            while node.data != before_data:
                node = node.prev
                if node is None:
                    return False
            new_node = Node(data)

            before_node = node.prev
            before_node.next = new_node
            new_node.prev = before_node
            new_node.next = node
            node.prev = new_node
            return True

    def insert_after(self, data, after_data):
        if self.head is None:
            self.head = Node(data)
            return True
        else:
            node = self.head
            while node.data != after_data:
                node = node.next
                if node is None:
                    return False
            new_node = Node(data)

            after_node = node.next
            new_node.next = after_node
            new_node.prev = node
            node.next = new_node
            if new_node.next is None:
                self.tail = new_node
            return True


    def print(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next


doublelist = NodeMgmt(0)
for i in range(1, 10):
    doublelist.insert(i)
#doublelist.insert_before(1.5, 2)
doublelist.insert_after(33, 4)
doublelist.print()