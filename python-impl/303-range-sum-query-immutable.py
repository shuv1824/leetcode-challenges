# https://leetcode.com/problems/range-sum-query-immutable/

import ast
from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = [0]
        for num in nums:
            self.prefix.append(self.prefix[-1] + num)

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right + 1] - self.prefix[left]


def main():
    while True:
        methods_input = input("Enter methods list: ")
        arguments_input = input("Enter arguments list: ")

        methods = ast.literal_eval(methods_input)
        arguments = ast.literal_eval(arguments_input)

        output = []

        obj = None

        for method, arg in zip(methods, arguments):
            if method == "NumArray":
                obj = NumArray(*arg)
                output.append(None)
            else:
                result = getattr(obj, method)(*arg)
                output.append(result)

        print(output)


if __name__ == "__main__":
    main()
