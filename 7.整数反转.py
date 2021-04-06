#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        a = str(x).replace('-','')
        a = int(a[::-1])
        if a < 2**31:
            if x < 0:
                return -a
            else:
                return a
        else:
            return 0
# @lc code=end

