# https://leetcode.com/problems/repeated-substring-pattern/description/


def repeatedSubstringPattern(s: str) -> bool:
    if not s:
        return False
    return s in (s + s)[1:-1]


def main():
    while True:
        s = input("Enter string s: ")
        res = repeatedSubstringPattern(s)
        print(res)


if __name__ == "__main__":
    main()
