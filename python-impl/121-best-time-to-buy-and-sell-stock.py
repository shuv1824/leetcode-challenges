from typing import List


def maxProfit(prices: List[int]) -> int:
    l, r = 0, 1
    maxP = 0

    while r < len(prices):
        if prices[l] < prices[r]:
            maxP = max(maxP, prices[r] - prices[l])
        else:
            l = r
        r += 1

    return maxP


def main():
    while True:
        nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
        res = maxProfit(nums)
        print(res)


if __name__ == "__main__":
    main()
