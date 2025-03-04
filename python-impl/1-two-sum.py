# https://leetcode.com/problems/two-sum/description/
from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    numMap = {val: i for i, val in enumerate(nums)}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in numMap.keys() and numMap[complement] != i:
            return [i, numMap[complement]]


def main():
    while True:
        nums = list(
            map(int, input("Enter numbers separated by spaces: ").split()))
        target = int(input("Enter a target number: "))
        res = twoSum(nums, target)
        print(res)


if __name__ == "__main__":
    main()
