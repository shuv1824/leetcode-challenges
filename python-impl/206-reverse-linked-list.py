# https://leetcode.com/problems/reverse-linked-list/description/
from typing import Optional, List


class ListNode:
    def __init__(self, value=0, next=None):
        self.val = value
        self.next = next


def create_linked_list(lst: List[int]) -> Optional[ListNode]:
    linkedList = ListNode()

    current = linkedList

    for i in range(len(lst)):
        current.next = ListNode(lst[i])
        current = current.next

    return linkedList.next


def list_from_nodes(head: Optional[ListNode]) -> List[int]:
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    current = head
    prev = None

    while current:
        temp = None
        if current.next:
            temp = current.next
        current.next = prev
        prev = current
        current = temp

    return prev


def main():
    while True:
        list_input = list(
            map(int, input("Enter numbers separated by spaces for list: ").split())
        )

        head = create_linked_list(list_input)

        reversedList = reverseList(head)

        print(list_from_nodes(reversedList))


if __name__ == "__main__":
    main()
