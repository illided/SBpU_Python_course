from collections import MutableMapping
from typing import Iterator, Callable, Any, Tuple, Optional, TypeVar
from random import randint
from abc import ABCMeta, abstractmethod


class Comparable(metaclass=ABCMeta):
    @abstractmethod
    def __lt__(self, other: Any) -> bool:
        ...

    @abstractmethod
    def __gt__(self, other: Any) -> bool:
        ...


CT = TypeVar("CT", bound=Comparable)


class Node:
    """
    Information unit of deramida.
    Holds key, value, priority and its children.
    """

    priority: int
    key: CT
    value: Any
    left_child: Optional["Node"]
    right_child: Optional["Node"]

    def __init__(self, key: CT, value: Any):
        self.key = key
        self.value = value
        self.left_child = None
        self.right_child = None
        self.priority = randint(0, 100)

    def inorder(self) -> Iterator["Node"]:
        nodes = []
        if self.have_left_child():
            nodes.extend(list(self.left_child.inorder()))
        nodes.append(self)
        if self.have_right_child():
            nodes.extend(list(self.right_child.inorder()))
        return iter(nodes)

    def reverse_inorder(self) -> Iterator["Node"]:
        nodes = []
        if self.have_right_child():
            nodes.extend(list(self.right_child.reverse_inorder()))
        nodes.append(self)
        if self.have_left_child():
            nodes.extend(list(self.left_child.reverse_inorder()))
        return iter(nodes)

    def have_left_child(self) -> bool:
        return self.left_child is not None

    def have_right_child(self) -> bool:
        return self.right_child is not None


class Deramida(MutableMapping):
    """
    Deramida is a data structure that combines a binary search tree and a binary heap.
    Mostly it behaves like a dict, but keys must be comparable.
    When iterating through deramida, items will be returned in ascending order of keys.
    """

    root: Optional[Node]
    __size: int

    def split(self, node: Optional[Node], key: CT) -> Tuple[Optional[Node], Optional[Node]]:
        if node is None:
            return None, None
        elif key > node.key:
            left, right = self.split(node.right_child, key)
            node.right_child = left
            return node, right
        elif key < node.key:
            left, right = self.split(node.left_child, key)
            node.left_child = right
            return left, node
        return node.left_child, node.right_child

    def merge(self, small_keys_s_tree: Optional[Node], big_keys_s_tree: Optional[Node]) -> Node:
        if small_keys_s_tree is None:
            return big_keys_s_tree
        if big_keys_s_tree is None:
            return small_keys_s_tree
        if small_keys_s_tree.priority > big_keys_s_tree.priority:
            small_keys_s_tree.right_child = self.merge(small_keys_s_tree.right_child, big_keys_s_tree)
            return small_keys_s_tree
        big_keys_s_tree.left_child = self.merge(small_keys_s_tree, big_keys_s_tree.left_child)
        return big_keys_s_tree

    def __init__(self):
        self.__size = 0
        self.root = None

    def __contains__(self, key: Any) -> bool:
        return self.find_node(key, lambda x: x.key == key) is not None

    def __setitem__(self, key: CT, value: Any) -> None:
        if key not in self:
            self.__size += 1
        left, right = self.split(self.root, key)
        new_node = Node(key, value)
        left = self.merge(left, new_node)
        self.root = self.merge(left, right)

    def __delitem__(self, key: CT) -> None:
        if key not in self:
            raise KeyError(f"No key for value {key}")
        self.__size -= 1
        left, right = self.split(self.root, key)
        self.root = self.merge(left, right)

    def find_node(self, key: CT, condition: Callable[[Node], bool]):
        current_node = self.root
        while current_node is not None:
            if condition(current_node):
                return current_node
            if key > current_node.key:
                current_node = current_node.right_child
            else:
                current_node = current_node.left_child
        return None

    def __getitem__(self, key: CT) -> Any:
        node = self.find_node(key, lambda x: x.key == key)
        if node is None:
            raise KeyError(f"No key for value {key}")
        else:
            return node.value

    def __len__(self) -> int:
        return self.__size

    def __iter__(self) -> Iterator[Node]:
        if self:
            for node in self.root.inorder():
                yield node.value
        return iter(())

    def __reversed__(self) -> Iterator[Node]:
        if self:
            for node in self.root.reverse_inorder():
                yield node.value
        return iter(())
