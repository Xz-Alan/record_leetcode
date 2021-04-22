#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 动态规划
        '''
        pre, ans = 0, nums[0]
        for i in range(len(nums)):
            pre = max(pre + nums[i], nums[i])
            ans = max(ans, pre)
        return ans
        '''
        # 前缀和
        # sum(i, j) = sum(0, j) - sum(0, i)
        cur_sum = 0
        min_sum = 0
        res = float("-inf")
        for num in nums:
            cur_sum += num
            res = max(res, cur_sum - min_sum)
            min_sum = min(min_sum, cur_sum)
        return res
# @lc code=end

