#
# @lc app=leetcode.cn id=1049 lang=python3
#
# [1049] 最后一块石头的重量 II
#

# @lc code=start
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        dp = [0 for _ in range(total // 2 + 1)]
        for stone in stones:
            for j in range(total // 2, stone - 1, -1):
                dp[j] = max(dp[j], dp[j - stone] + stone)
        return total - dp[total // 2] * 2
# @lc code=end

