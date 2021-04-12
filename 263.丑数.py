#
# @lc app=leetcode.cn id=263 lang=python3
#
# [263] 丑数
#

# @lc code=start
class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        factors = [2,3,5]
        for factor in factors:
            while n % factor == 0:
                n //= factor
        return n == 1
# @lc code=end

