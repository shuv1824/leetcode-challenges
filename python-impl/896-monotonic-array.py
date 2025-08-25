# https://leetcode.com/problems/monotonic-array/description/
from typing import List


def isMonotonic(nums: List[int]) -> bool:
    return all(nums[i] <= nums[i + 1] for i in range(len(nums) - 1)) or all(
        nums[i] >= nums[i + 1] for i in range(len(nums) - 1)
    )


def main():
    while True:
        nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
        res = isMonotonic(nums)
        print(res)


if __name__ == "__main__":
    main()
