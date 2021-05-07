#
# @lc app=leetcode.cn id=1486 lang=python3
#
# [1486] 数组异或操作
#

# @lc code=start
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        '''
        ans = start
        for i in range(1, n):
            ans ^= (start + i * 2)
        return ans
        '''
        def sumXor(x):
            if x % 4 == 0:
                return x
            if x % 4 == 1:
                return 1
            if x % 4 == 3:
                return 0
            return x+1
        e = n & start & 1
        s = start >> 1
        ans = sumXor(s - 1) ^ sumXor(s + n - 1)
        return ans << 1 | e
# @lc code=end

