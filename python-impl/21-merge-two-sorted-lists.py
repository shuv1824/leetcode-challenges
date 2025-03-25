# https://leetcode.com/problems/merge-two-sorted-lists/description/
from typing import Optional, List


class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def create_linked_list(lst: List[int]) -> Optional[ListNode]:
    dummy = ListNode()
    current = dummy

    for num in lst:
        current.next = ListNode(num)
        current = current.next

    return dummy.next


def list_from_nodes(head: Optional[ListNode]) -> List[int]:
    result = []
    current = head
    while current:
        result.append(current.value)
        current = current.next
    return result


def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    mergedList = ListNode()
    current = mergedList

    while list1 and list2:
        if list1.value <= list2.value:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next

        current = current.next

    current.next = list1 if list1 else list2

    return mergedList.next


def main():
    while True:
        list1_input = list(
            map(int, input("Enter numbers separated by spaces for list1: ").split()))
        list1 = create_linked_list(list1_input)

        list2_input = list(
            map(int, input("Enter numbers separated by spaces for list2: ").split()))
        list2 = create_linked_list(list2_input)

        merged_head = mergeTwoLists(list1, list2)
        merged_list = list_from_nodes(merged_head)

        print(merged_list)


if __name__ == "__main__":
    main()
