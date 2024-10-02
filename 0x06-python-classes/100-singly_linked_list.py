#!/usr/bin/python3
"""
This module defines a Node and a SinglyLinkedList class.
"""


class Node:
    """
    This class represents a node of a singly linked list.
    """

    def __init__(self, data, next_node=None):
        """
        Initializes the Node with data and next_node.
        Args:
            data (int): The data of the node.
            next_node (Node): The next node in the list.
        Raises:
            TypeError: If data is not an integer or next_node is not a Node object.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Retrieves the data of the node.
        Returns:
            int: The data of the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Sets the data of the node.
        Args:
            value (int): The data of the node.
        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Retrieves the next node.
        Returns:
            Node: The next node in the list.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Sets the next node.
        Args:
            value (Node): The next node in the list.
        Raises:
            TypeError: If value is not None or a Node object.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    This class represents a singly linked list.
    """

    def __init__(self):
        """
        Initializes the singly linked list.
        """
        self.__head = None

    def __str__(self):
        """
        Defines the string representation of the singly linked list.
        Returns:
            str: The string representation of the list.
        """
        result = []
        current = self.__head
        while current is not None:
            result.append(str(current.data))
            current = current.next_node
        return "\n".join(result)

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position in the list (increasing order).
        Args:
            value (int): The value to insert.
        """
        new_node = Node(value)
        if self.__head is None or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node
