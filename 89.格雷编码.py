#
# @lc app=leetcode.cn id=89 lang=python3
#
# [89] 格雷编码
#

# @lc code=start
class Solution:
    def grayCode(self, n: int) -> List[int]:
        return [i^(i>>1) for i in range(1<<n)]
        '''
        range(1<<n) <==> range(2**n)
        '''
# @lc code=end

