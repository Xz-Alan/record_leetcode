#
# @lc app=leetcode.cn id=31 lang=python3
#
# [31] 下一个排列
#

# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        题干含义：找出这个数组排序出的所有数中，刚好比当前数大的下一个数
        如：132486 --> 132648
        """
        for i in range(len(nums)-2, -1 , -1):   # 从列表倒数第二个数从右向左循环
            if nums[i] < nums[i+1]:
                for j in range(len(nums)-1, i, -1):
                    if nums[j] > nums[i]:
                        nums[i], nums[j] = nums[j], nums[i]
                        nums[i+1:] = sorted(nums[i+1:])
                        return
        return nums.sort()
# @lc code=end

