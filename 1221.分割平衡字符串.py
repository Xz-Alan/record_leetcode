#
# @lc app=leetcode.cn id=1221 lang=python3
#
# [1221] 分割平衡字符串
#

# @lc code=start
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        num, length = 0, 0
        for i in s:
            if i == 'L':
                length += 1
            else :
                length -= 1
            if length == 0:
                num += 1
        return num

# @lc code=end

