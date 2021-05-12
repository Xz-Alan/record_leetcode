#
# @lc app=leetcode.cn id=1734 lang=python3
#
# [1734] 解码异或后的排列
#

# @lc code=start
class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        n =  len(encoded) + 1
        total = reduce(xor, range(1, n + 1))
        odd = 0
        for i in range(1, n - 1, 2):
            odd ^= encoded[i]
        perm = [total ^ odd] * (n)
        for i in range(1, n):
            perm[i] = perm[i - 1] ^ encoded[i - 1]
        return perm

# @lc code=end

