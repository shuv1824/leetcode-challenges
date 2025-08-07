# https://leetcode.com/problems/matrix-diagonal-sum/

from typing import List


def diagonalSum(mat: List[List[int]]) -> int:
    sum = 0

    for i in range(len(mat)):
        sum += mat[i][i] + mat[i][len(mat) - i - 1]
    if len(mat) % 2 != 0:
        sum -= mat[len(mat) // 2][len(mat) // 2]

    return sum


def main():
    while True:
        rows = int(input("Enter number of rows: "))
        matrix = [
            list(map(int, input("Enter numbers separated by spaces as rows: ").split()))
            for _ in range(rows)
        ]
        res = diagonalSum(matrix)
        print(res)


if __name__ == "__main__":
    main()
