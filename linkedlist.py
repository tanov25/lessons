class Node:
    def __init__(self, v):
        self.value = v
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node != None:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        list_of_nodes = []
        node = self.head
        while node is not None:
            if node.value == val:
                list_of_nodes.append(node)
            node = node.next
        return list_of_nodes

    def delete(self, val, all=False):
        prev_node = None
        node = self.head
        last_deleted = None
        while node is not None:
            if node.value == val:
                if not prev_node:
                    self.head = node.next
                else:
                    prev_node.next = node.next
                if not node.next:
                    self.tail = prev_node
                if not all:
                    return
                else:
                    last_deleted = node
            if node != last_deleted:
                prev_node = node
            node = node.next

    def clean(self):
        self.head = None
        self.tail = None

    def len(self):
        list_len = 0
        node = self.head
        while node is not None:
            list_len += 1
            node = node.next
        return list_len

    def insert(self, afterNode, newNode):
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            return
        node = self.head
        found = False
        while node is not None:
            if node == afterNode:
                found = True
                newNode.next = node.next
                node.next = newNode
                break
            node = node.next
        if afterNode == self.tail:
            self.tail = newNode
        if not found:
            newNode.next = self.head
            self.head = newNode
