#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            a = target - nums[i]
            if a in dic:
                return dic[a],i
            dic[nums[i]] = i
# @lc code=end

