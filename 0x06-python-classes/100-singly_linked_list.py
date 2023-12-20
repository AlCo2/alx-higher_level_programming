#!/usr/bin/python3

"""singly linked list project"""


class Node:
    """this is the representation of a class"""
    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """this is the singly linked list class"""
    def __init__(self):
        self.__head = None

    def __str__(self):
        temp = self.__head
        while temp:
            print(temp.data)
            temp = temp.next_node
        return ""

    def sorted_insert(self, value):
        new_node = Node(value, None)
        if self.__head is None:
            self.__head = new_node
        else:
            temp = self.__head
            if (temp.next_node is None):
                if temp.data < new_node.data:
                    temp.next_node = new_node
                else:
                    new_node.next_node = temp
                    self.__head = new_node
            else:
                if (temp.data > new_node.data):
                    new_node.next_node = temp
                    self.__head = new_node
                else:
                    while (temp.next_node is not None
                            and temp.next_node.data < new_node.data):
                        temp = temp.next_node
                    last = temp.next_node
                    temp.next_node = new_node
                    new_node.next_node = last
