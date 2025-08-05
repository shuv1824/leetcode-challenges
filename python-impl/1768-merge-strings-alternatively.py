# https://leetcode.com/problems/merge-strings-alternately/


def mergeAlternately(word1: str, word2: str) -> str:
    res = ""
    i = 0
    j = 0

    while True:
        if i < len(word1):
            res += word1[i]
            i += 1

        if j < len(word2):
            res += word2[j]
            j += 1

        if (i == len(word1)) and (j == len(word2)):
            break

    return res


def main():
    while True:
        word1 = input("Enter word 1: ")
        word2 = input("Enter word 2: ")
        res = mergeAlternately(word1, word2)
        print(res)


if __name__ == "__main__":
    main()
