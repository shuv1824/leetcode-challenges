# https://leetcode.com/problems/climbing-stairs/description/


def climbStairs(n: int) -> int:
    if n <= 2:
        return n

    # Brute force recursion
    # return climbStairs(n-1) + climbStairs(n-2)

    # Optimization: Tabulation
    dp = [0] * (n + 1)
    dp[0] = dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


def main():
    while True:
        n = input("Enter a number: ")
        res = climbStairs(int(n))
        print(res)


if __name__ == "__main__":
    main()
