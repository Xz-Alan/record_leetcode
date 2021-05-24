#
# @lc app=leetcode.cn id=664 lang=python3
#
# [664] 奇怪的打印机
#

# @lc code=start
class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        dp = [[0] * (n) for _ in range(n)]
        for i in range(n - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i][j - 1]
                else:
                    min_dp = 10000
                    for k in range(i, j):
                        min_dp = min(min_dp, dp[i][k] + dp[k + 1][j])
                    dp[i][j] = min_dp
        return dp[0][n - 1]


# @lc code=end

