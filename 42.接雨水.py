#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        block = sum(height)
        left, right = 0, len(height) - 1
        total, high = 0, 1
        while(left <= right):
            while(left <= right and height[left] < high):
                left += 1
            while(left <= right and height[right] < high):
                right -= 1
            total += right - left + 1
            high += 1
        return total - block
# @lc code=end

