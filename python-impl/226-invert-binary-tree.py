from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def create_tree(lst: List[int]) -> Optional[TreeNode]:
    if not lst:
        return None

    root = TreeNode(lst[0])
    queue = deque([root])
    i = 1

    while queue and i < len(lst):
        node = queue.popleft()

        if lst[i] is not None:
            node.left = TreeNode(lst[i])
            queue.append(node.left)

        i += 1

        if i < len(lst) and lst[i] is not None:
            node.right = TreeNode(lst[i])
            queue.append(node.right)

        i += 1

    return root


def list_from_root(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []

    queue = deque([root])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node.val)

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)

    return result


def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if root:
        root.left, root.right = invertTree(root.right), invertTree(root.left)
    return root


def main():
    while True:
        list_input = list(
            map(int, input("Enter numbers separated by spaces for list: ").split())
        )

        root = create_tree(list_input)

        inverted_tree = invertTree(root)

        print(list_from_root(inverted_tree))


if __name__ == "__main__":
    main()
