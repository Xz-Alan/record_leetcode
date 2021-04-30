#
# @lc app=leetcode.cn id=137 lang=python3
#
# [137] 只出现一次的数字 II
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash_nums = collections.Counter(nums)
        return [num for num, count in hash_nums.items() if count == 1][0]
# @lc code=end

