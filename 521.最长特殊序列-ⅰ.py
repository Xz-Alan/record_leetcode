#
# @lc app=leetcode.cn id=521 lang=python3
#
# [521] 最长特殊序列 Ⅰ
#

# @lc code=start
class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        return -1 if a == b else max(len(a), len(b))
# @lc code=end


a = "aba"
b = "aba"
sol = Solution().findLUSlength(a, b)
print(sol)
