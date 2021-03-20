"""
Linked Lists consists of Nodes.
Nodes contain data and also may link to other nodes:
    - Head Node: First node, the address of the
                 head node gives us access of the complete list
    - Last node: points to null
"""

from typing import Any   # 类型注解 typing库 详见https://www.jb51.net/article/166907.htm


class Node:      #定义一个节点
    def __init__(self, item: Any, next: Any) -> None:   # item和next的类型是any 返回值类型是none
        self.item = item
        self.next = next


class LinkedList:    # 定义一个链表
    def __init__(self) -> None:
        self.head = None
        self.size = 0     # 链表长度

    def add(self, item: Any) -> None:
        self.head = Node(item, self.head)
        self.size += 1

    def remove(self) -> Any:
        if self.is_empty():
            return None
        else:
            item = self.head.item
            self.head = self.head.next
            self.size -= 1
            return item

    def is_empty(self) -> bool:
        return self.head is None

    def __str__(self) -> str:
        """
                头插新节点
        >>> linked_list = LinkedList()
        >>> linked_list.add(23)
        >>> linked_list.add(14)
        >>> linked_list.add(9)
        >>> print(linked_list)
        9 --> 14 --> 23
        """
        if not self.is_empty:
            return ""
        else:
            iterate = self.head
            item_str = ""
            item_list = []
            while iterate:
                item_list.append(str(iterate.item))
                iterate = iterate.next

            item_str = " --> ".join(item_list)

            return item_str

    def __len__(self) -> int:
        """
        >>> linked_list = LinkedList()
        >>> len(linked_list)
        0
        >>> linked_list.add("a")
        >>> len(linked_list)
        1
        >>> linked_list.add("b")
        >>> len(linked_list)
        2
        >>> _ = linked_list.remove()
        >>> len(linked_list)
        1
        >>> _ = linked_list.remove()
        >>> len(linked_list)
        0
        """
        return self.size
