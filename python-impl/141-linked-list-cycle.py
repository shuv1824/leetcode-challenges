# https://leetcode.com/problems/linked-list-cycle/description/
from typing import Optional, List


class ListNode:
    def __init__(self, value=0, next=None):
        self.val = value
        self.next = next


def create_linked_list(lst: List[int]) -> Optional[ListNode]:
    dummy = ListNode()
    current = dummy

    for num in lst:
        current.next = ListNode(num)
        current = current.next

    return dummy.next


def hasCycle(head: Optional[ListNode]) -> bool:
    if not head or not head.next:
        return False
    current = head
    nxt = current.next

    while current or nxt:
        if current.val == nxt.val:
            return True
        current = current.next
        nxt = nxt.next.next

    return False


def main():
    while True:
        list1_input = list(
            map(int, input("Enter numbers separated by spaces for list1: ").split())
        )
        list1 = create_linked_list(list1_input)


if __name__ == "__main__":
    main()
