# https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/


def countOdds(low: int, high: int) -> int:
    return int((high - low) / 2 + (low & 1 | high & 1))


def main():
    while True:
        low = int(input("Enter a number for low: "))
        high = int(input("Enter a number for high: "))
        res = countOdds(low, high)
        print(res)


if __name__ == "__main__":
    main()
