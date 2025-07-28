# https://leetcode.com/problems/maximum-ascending-subarray-sum/description/
from typing import List


def maxAscendingSum(nums: List[int]) -> int:
    current = maxSum = nums[0]

    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            current += nums[i]
        else:
            current = nums[i]
        maxSum = max(maxSum, current)

    return maxSum


def main():
    while True:
        nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
        res = maxAscendingSum(nums)
        print(res)


if __name__ == "__main__":
    main()
