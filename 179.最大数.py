#
# @lc app=leetcode.cn id=179 lang=python3
#
# [179] 最大数
#

# @lc code=start
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = sorted(map(str, nums), key=cmp_to_key(lambda x, y : int(y + x) - int(x + y)))
        # lambda x, y : 1 if x + y < y + x else -1
        return "0" if nums[0] == "0" else "".join(nums)
# @lc code=end

