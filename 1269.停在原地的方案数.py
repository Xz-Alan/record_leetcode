#
# @lc app=leetcode.cn id=1269 lang=python3
#
# [1269] 停在原地的方案数
#

# @lc code=start
class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        mod = 10 ** 9 + 7
        max_column = min(steps, arrLen - 1)
        dp = [0] * (max_column + 1)
        dp[0] = 1
        for i in range(1, steps + 1):
            dp_next = [0] * (max_column + 1)
            for j in range(max_column + 1):
                dp_next[j] = dp[j]
                if j - 1 >= 0:
                    dp_next[j] += dp[j - 1]
                if j + 1 <= max_column:
                    dp_next[j] += dp[j + 1]
                dp_next[j] %= mod
            dp = dp_next
        return dp[0]
# @lc code=end

