#
# @lc app=leetcode.cn id=740 lang=python3
#
# [740] 删除与获得点数
#

# @lc code=start
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        max_nums = max(nums)
        sum_nums = [0] * (max_nums + 1)
        for num in nums:
            sum_nums[num] += num

        def rob(nums):
            size = len(nums)
            first, second = nums[0], max(nums[0], nums[1])
            for i in range(2, size):
                first, second = second, max(nums[i] + first, second)
            return second
        
        return rob(sum_nums)
# @lc code=end

