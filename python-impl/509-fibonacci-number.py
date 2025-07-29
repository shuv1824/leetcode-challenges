# https://leetcode.com/problems/fibonacci-number/description/


def fib(n: int) -> int:
    if n <= 1:
        return n

    dp = [0] * (n + 1)
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


def main():
    while True:
        n = input("Enter a number: ")
        res = fib(int(n))
        print(res)


if __name__ == "__main__":
    main()
