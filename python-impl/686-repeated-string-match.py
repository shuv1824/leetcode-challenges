# https://leetcode.com/problems/repeated-string-match/


def repeatedStringMatch(a: str, b: str) -> int:
    f = (len(b) - 1) // len(a) + 1

    for i in range(2):
        if b in a * (f + i):
            return f + i

    return -1


def main():
    while True:
        a = input("Enter string a: ")
        b = input("Enter string a: ")
        res = repeatedStringMatch(a, b)
        print(res)


if __name__ == "__main__":
    main()
