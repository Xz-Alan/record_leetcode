#
# @lc app=leetcode.cn id=461 lang=python3
#
# [461] 汉明距离
#

# @lc code=start
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # return bin(x ^ y).count('1')
        s, ans = x ^ y, 0
        while(s):
            ans += s & 1
            s >>= 1
        return ans

# @lc code=end

