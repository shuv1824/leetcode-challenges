# https://leetcode.com/problems/merge-two-sorted-lists/description/
from typing import Optional


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        values = []
        temp = self.head
        while temp:
            values.append(temp.value)
            temp = temp.next
        return str(values)

    def insert(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node


def mergeTwoLists(list1: Optional[LinkedList], list2: Optional[LinkedList]) -> Optional[LinkedList]:
    pass


def main():
    while True:
        linkedlist1 = LinkedList()
        linkedlist2 = LinkedList()

        list1 = list(
            map(int, input("Enter numbers separated by spaces for list1: ").split()))
        list2 = list(
            map(int, input("Enter numbers separated by spaces for list2: ").split()))

        for val in list1:
            linkedlist1.insert(val)
        for val in list2:
            linkedlist2.insert(val)

        mergedList = mergeTwoLists(linkedlist1, linkedlist2)
        print(mergedList)


if __name__ == "__main__":
    main()
