# https://leetcode.com/problems/find-the-difference/


def findTheDifference(s: str, t: str) -> str:
    res = t
    for c in s:
        res = res.replace(c, "", 1)
    return res


def main():
    while True:
        s = input("Enter string s: ")
        t = input("Enter string t: ")
        res = findTheDifference(s, t)
        print(res)


if __name__ == "__main__":
    main()
