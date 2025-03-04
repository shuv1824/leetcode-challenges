# https://leetcode.com/problems/move-zeroes/
from typing import List


def moveZeroesSlow(nums: List[int]) -> None:
    start, end = 0, len(nums)-1
    while start < end:
        if nums[start] == 0:
            for i in range(start, end):
                nums[i] = nums[i+1]
            nums[end] = 0
            end = end - 1
        if nums[start] != 0:
            start = start + 1

    print(nums)


def moveZeroesFast(nums: List[int]) -> None:
    j = 0
    for i in range(len(nums)):
        if nums[i] != 0 and nums[j] == 0:
            nums[j], nums[i] = nums[i], nums[j]

        if nums[j] != 0:
            j += 1

    print(nums)


def main():
    while True:
        nums = list(
            map(int, input("Enter numbers separated by spaces: ").split()))
        moveZeroesFast(nums)


if __name__ == "__main__":
    main()
