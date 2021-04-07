from collections import MutableMapping
from typing import Iterator, Callable, Any
from random import randint


class Node:
    priority: int

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left_child = None
        self.right_child = None
        self.priority = randint(0, 100)

    def inorder(self) -> list:
        values = []
        if self.left_child is not None:
            values.extend(self.left_child.inorder())
        values.append(self.value)
        if self.right_child is not None:
            values.extend(self.right_child.inorder())
        return values


def split(node: Node, key):
    if node is None:
        return None, None
    elif key > node.key:
        left, right = split(node.right_child, key)
        node.right_child = left
        return node, right
    elif key < node.key:
        left, right = split(node.left_child, key)
        node.left_child = right
        return left, node
    else:
        return node.left_child, node.right_child


def merge(first: Node, second: Node):
    if first is None:
        return second
    if second is None:
        return first
    if first.priority > second.priority:
        first.right_child = merge(first.right_child, second)
        return first
    else:
        second.left_child = merge(first, second.left_child)
        return second


class Deramida(MutableMapping):
    root: Node = None
    __size: int

    def __init__(self):
        self.__size = 0

    def __contains__(self, key):
        try:
            a = self[key]
            return True
        except KeyError:
            return False

    def __setitem__(self, key, value) -> None:
        if key not in self:
            self.__size += 1
        left, right = split(self.root, key)
        new_node = Node(key, value)
        left = merge(left, new_node)
        self.root = merge(left, right)

    def __delitem__(self, key) -> None:
        if key not in self:
            raise KeyError(f"No key for value {key}")
        self.__size -= 1
        left, right = split(self.root, key)
        self.root = merge(left, right)

    def find_node(self, key, condition: Callable[[Node], bool]):
        current_node = self.root
        while current_node is not None:
            if condition(current_node):
                return current_node
            if key > current_node.key:
                current_node = current_node.right_child
            else:
                current_node = current_node.left_child
        return None

    def __getitem__(self, key) -> Any:
        node = self.find_node(key, lambda x: x.key == key)
        if node is None:
            raise KeyError(f"No key for value {key}")
        else:
            return node.value

    def __len__(self) -> int:
        return self.__size

    def __iter__(self) -> Iterator:
        root_values = []
        if len(self) != 0:
            root_values = self.root.inorder()
        for val in root_values:
            yield val

    def __reversed__(self) -> Iterator:
        root_values = []
        if len(self) != 0:
            root_values = self.root.inorder()
        return reversed(root_values)
