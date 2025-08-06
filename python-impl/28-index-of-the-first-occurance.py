# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/


def findindex(haystack: str, needle: str) -> int:
    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i : i + len(needle)] == needle:
            return i
    return -1


def main():
    while True:
        haystack = input("Enter string for haystack: ")
        needle = input("Enter string for needle: ")
        res = findindex(haystack, needle)
        print(res)


if __name__ == "__main__":
    main()
