# https://leetcode.com/problems/linked-list-cycle/description/
from typing import Optional, List


class ListNode:
    def __init__(self, value=0, next=None):
        self.val = value
        self.next = next


def create_linked_list(lst: List[int], pos: int) -> Optional[ListNode]:
    linkedList = ListNode()
    temp = None

    current = linkedList

    for i in range(len(lst)):
        current.next = ListNode(lst[i])
        current = current.next

        if i == pos:
            temp = current

        if i == len(lst) - 1:
            current.next = temp

    return linkedList.next


def hasCycle(head: Optional[ListNode]) -> bool:
    current = nxt = head

    while nxt and nxt.next:
        current = current.next
        nxt = nxt.next.next

        if current == nxt:
            return True

    return False


def main():
    while True:
        list_input = list(
            map(int, input("Enter numbers separated by spaces for list: ").split())
        )
        pos = input("Enter a pos: ")

        head = create_linked_list(list_input, int(pos))

        print(hasCycle(head))


if __name__ == "__main__":
    main()
