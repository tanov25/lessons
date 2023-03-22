import unittest


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


class TestLinkedList(unittest.TestCase):

    def test_clean(self):
        l = LinkedList()
        for i in range(0, 10):
            l.add_in_tail(Node(i))
        l.clean()
        self.assertEqual(l.head, None)
        self.assertEqual(l.tail, None)

    def test_insert(self):
        l = LinkedList()
        node = Node(1)
        l.insert(Node(0), node)
        self.assertEqual(l.len(), 1)

    def test_insert1(self):
        l = LinkedList()
        node = Node(1)
        node2 = Node(2)
        l.insert(Node(0), node)
        l.insert(node, node2)
        self.assertEqual(l.len(), 2)
        self.assertEqual(node, l.head)
        self.assertEqual(node2, l.tail)

    def test_find_all(self):
        l = LinkedList()
        nodes = [Node(0) for i in range(0, 15)]
        for node in nodes:
            l.insert(node, node)
        nodes_copy = l.find_all(0)
        nodes_1 = l.find_all(1)
        self.assertEqual(list(reversed(nodes_copy)), nodes)
        self.assertEqual(nodes_1, [])

    def test_find_all(self):
        l = LinkedList()
        vals = [0, 1, 2, 0, 1, 1, 3, 5, 4]
        nodes = [Node(i) for i in vals]
        for node in nodes:
            l.add_in_tail(node)
        find1 = l.find_all(1)
        find2 = l.find_all(-1)
        self.assertEqual(len(find1), 3)
        self.assertEqual(len(find2), 0)

    def test_insert2(self):
        l = LinkedList()
        vals = range(0, 10)
        nodes = [Node(i) for i in vals]
        for node in nodes:
            l.add_in_tail(node)
        node = nodes[3]
        l.insert(node, Node(12))
        node1 = nodes[6]
        l.insert(node1, Node(17))
        node2 = nodes[-1]
        l.insert(node2, Node(23))
        self.assertEqual(node.next.value, 12)
        self.assertEqual(node1.next.value, 17)
        self.assertEqual(node2.next.value, 23)
        self.assertEqual(l.tail.value, 23)

    def test_delete(self):
        l = LinkedList()
        vals = range(0, 10)
        nodes = [Node(i) for i in vals]
        for node in nodes:
            l.add_in_tail(node)
        l.delete(0, True)
        l.delete(15, True)
        l.delete(-1)
        self.assertEqual(l.head.value, 1)
        self.assertEqual(l.len(), 9)

    def test_delete1(self):
        l = LinkedList()
        vals = range(0, 10)
        nodes = [Node(i) for i in vals]
        for node in nodes:
            l.add_in_tail(node)
        l.delete(0, True)
        l.insert(nodes[0], Node(9))
        self.assertEqual(l.head.value, 9)

    def test_delete2(self):
        l = LinkedList()
        vals = range(0, 10)
        nodes = [Node(i) for i in vals]
        for node in nodes:
            l.add_in_tail(node)
        l.delete(0, True)
        l.insert(nodes[0], Node(9))
        l.delete(9, True)
        self.assertEqual(l.head.value, 1)
        self.assertEqual(l.tail.value, 8)

    def test_delete3(self):
        l = LinkedList()
        vals = range(0, 10)
        nodes = [Node(i) for i in vals]
        for node in nodes:
            l.add_in_tail(node)
        l.delete(4)
        self.assertEqual(nodes[3].next.value, 5)
        l.clean()
        l.delete(4, True)
        self.assertEqual(l.len(), 0)

    def test_delete4(self):
        l = LinkedList()
        for i in range(0, 10):
            l.add_in_tail(Node(0))
        l.delete(0, True)
        self.assertEqual(l.len(), 0)
        self.assertEqual(l.head, None)
        self.assertEqual(l.tail, None)

    def test_delete5(self):
        l = LinkedList()
        for i in range(0, 10):
            l.add_in_tail(Node(0))
        l.add_in_tail(Node(1))
        l.delete(0, True)
        self.assertEqual(l.head.value, 1)
        self.assertEqual(l.tail.value, 1)
        l.delete(1, True)
        self.assertEqual(l.len(), 0)
        self.assertEqual(l.head, None)
        self.assertEqual(l.tail, None)


if __name__ == '__main__':
    unittest.main()
