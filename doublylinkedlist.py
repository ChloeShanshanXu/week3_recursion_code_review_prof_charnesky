# Code review from Dr Charnesky at:
# https://github.com/EricCharnesky/CIS2001-Winter2022/blob/main/LinkedLists/main.py

class CircularDoublyLinkedList:
    class Node:
        def __init__(self, data, next=None, previous=None):
            self.data = data
            self.next = next
            self.previous = previous

    def __init__(self):
        self._start = CircularDoublyLinkedList.Node(None)
        self._start.previous = self._start
        self._start.next = self._start
        self._number_of_items = 0

    def is_empty(self):
        return self._number_of_items == 0

    def __len__(self):
        return self._number_of_items

    def validata_index(self, index):
        if index < 0 or index >= len(self):
            raise IndexError

    def _add_node(self, data, next, previous):
        new_node = CircularDoublyLinkedList.Node(data, next, previous)
        new_node.next.previous = new_node
        new_node.previous.next = new_node
        self._number_of_items += 1

    def append(self, data):
        self._add_node(data, self._start, self._start.previous)

    def __setitem__(self, key, value):
        self.validata_index(key)
        current_index = 0
        current_node = self._start.next
        while current_index < key:
            current_index += 1
            current_node = current_node.next
        old_data = current_node.data
        current_node.data = value
        return old_data

    def __getitem__(self, key):
        self.validata_index(key)
        current_index = 0
        current_node = self._start.next
        while current_index < key:
            current_index += 1
            current_node = current_node.next
        return current_node.data

    def _remove_node(self, node):
        if self.is_empty():
            raise IndexError
        node.next.previous = node.previous
        node.previous.next = node.next
        self._number_of_items -= 1
        return node.data

    def pop(self, index=None):
        if index is None:
            return self._remove_node(self._start.previous)

        self.validata_index(index)
        current_index = 0
        current_node = self._start.next
        while current_index < index:
            current_node = current_node.next
            current_index += 1
        return self._remove_node(current_node)

    def insert(self, index, data):
        self.validata_index(index)
        current_index = 0
        current_node = self._start.next
        while current_index < index:
            current_index += 1
            current_node = self._start.next
        self._add_node(data, current_node, current_node.previous)

if __name__ =="__main__":
    ls = CircularDoublyLinkedList()
    for number in range(10):
        ls.append(number)
    for index in range(len(ls)):
        ls[index] = index*2
    for index in range(len(ls)):
        print(ls[index])