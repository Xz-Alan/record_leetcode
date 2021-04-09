#
# @lc app=leetcode.cn id=154 lang=python3
#
# [154] 寻找旋转排序数组中的最小值 II
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] == nums[r]:
                r -= 1
            elif nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1
        return nums[l]
# @lc code=end

