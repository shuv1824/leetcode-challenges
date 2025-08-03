# https://leetcode.com/problems/happy-number/description/


def getNext(n: int) -> int:
    return sum(int(ch) ** 2 for ch in str(n))


def isHappy(n: int) -> bool:
    slow = fast = n

    while True:
        slow = getNext(slow)
        fast = getNext(getNext(fast))

        if slow == fast:
            break

    return slow == 1


def main():
    while True:
        n = input("Enter a number: ")
        res = isHappy(int(n))
        print(res)


if __name__ == "__main__":
    main()
