#
# @lc app=leetcode.cn id=477 lang=python3
#
# [477] 汉明距离总和
#

# @lc code=start
class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        # 10^9 < 2^30
        for i in range(30):
            cnt = sum(((val >> i) & 1) for val in nums)
            ans += cnt * (n - cnt)
        return ans
# @lc code=end

