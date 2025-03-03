from typing import List


def containsDuplicate(nums: List[int]) -> bool:
    numset = set(nums)
    return len(nums) != len(numset)


def main():
    while True:
        nums = list(
            map(int, input("Enter numbers separated by spaces: ").split()))
        res = containsDuplicate(nums)
        print(res)


if __name__ == "__main__":
    main()
