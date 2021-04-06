#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1,-1]
        '''
        # 暴力扫描 时间复杂度 O(n)
        for i in range(len(nums)):
            if nums[i] == target:
                break
        for j in range(len(nums)-1,-1,-1):
            if nums[j] == target:
                break
        return [i, j]
        '''
        # 二分
        l, r = 0, len(nums) - 1
        while l < r:    # 找左边界 
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        res = [l]
        r = len(nums) - 1
        while l < r:    # 找右边界
            mid = (l + r + 1) // 2
            if nums[mid] > target:
                r = mid -1
            else:
                l = mid
        res.append(r)
        return res
# @lc code=end

