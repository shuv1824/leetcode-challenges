# https://leetcode.com/problems/valid-parentheses/


def isValid(s: str) -> bool:
    stack = list()

    for ch in s:
        if ch == "(" or ch == "{" or ch == "[":
            stack.append(ch)
        elif ch == ")" and len(stack) > 0 and stack[-1] == "(":
            stack.pop()
        elif ch == "}" and len(stack) > 0 and stack[-1] == "{":
            stack.pop()
        elif ch == "]" and len(stack) > 0 and stack[-1] == "[":
            stack.pop()
        else:
            return False

    return len(stack) == 0


def main():
    while True:
        s = input("Enter string s: ")
        res = isValid(s)
        print(res)


if __name__ == "__main__":
    main()
