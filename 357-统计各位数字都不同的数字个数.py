class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        # 打表
        # res = [1, 10, 91, 739, 5275, 32491, 168571, 712891, 2345851]
        # return res[n]
        # 排列组合
        # def permutation(m, n):
        #     res = 1
        #     i = m
        #     while i > m-n:
        #         res *= i
        #         i -= 1
        #     return res

        # dp = [1]*(n+1)
        # if n == 0:
        #     return dp[0]
        # for i in range(1, n+1):
        #     dp[i] = 9*permutation(9, i-1)+dp[i-1]
        # return dp[n]
        # 常数空间排列组合
        if n == 0:
            return 1
        if n == 1:
            return 10
        res, cur = 10, 9
        for i in range(n - 1):
            cur *= 9 - i
            res += cur
        return res
