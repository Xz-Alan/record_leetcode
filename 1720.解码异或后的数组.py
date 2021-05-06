#
# @lc app=leetcode.cn id=1720 lang=python3
#
# [1720] 解码异或后的数组
#

# @lc code=start
class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        n = len(encoded)
        ans = [first] * (n+1)
        for i in range(1, n + 1):
            ans[i] = ans[i - 1] ^ encoded[i - 1]
        return ans
# @lc code=end

