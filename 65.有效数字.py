#
# @lc app=leetcode.cn id=65 lang=python3
#
# [65] 有效数字
#

# @lc code=start
class Solution:
    def isNumber(self, s: str) -> bool:
        try:
            if "inf" in s.lower():
                return False
            float(s)
            return True
        except:
            return False
# @lc code=end

