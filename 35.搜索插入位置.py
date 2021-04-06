#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        '''
        # 暴力
        for i in range(len(nums)):
            if nums[i] >= target:
                return i 
        return len(nums)

        # 内置
        if target in nums:
            return nums.index(target)
        else:
            nums.append(target)
            nums.sort()
            return nums.index(target)
        '''
        # 二分
        l, r = 0, len(nums)
        while l < r :
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        return l
        
# @lc code=end

