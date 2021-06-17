#
# @lc app=leetcode.cn id=494 lang=python3
#
# [494] 目标和
#

# @lc code=start
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        n, diff = len(nums), total - target
        if (diff < 0 or diff % 2 !=0):
            return 0 
        neg = diff // 2
        dp = [[0] * (neg + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        for i in range(1, n + 1):
            num = nums[i - 1]
            for j in range(0, neg + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= num:
                    dp[i][j] += dp[i - 1][j - num]
        return dp[n][neg]
# @lc code=end

