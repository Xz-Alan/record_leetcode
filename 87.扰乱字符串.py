#
# @lc app=leetcode.cn id=87 lang=python3
#
# [87] 扰乱字符串
#

# @lc code=start
class Solution:
    # @cache
    @functools.lru_cache(None)
    def isScramble(self, s1: str, s2: str) -> bool:
        # 朴素递归 --> 超时 --> 记忆化递归 --> @cache/@functools.lru_cache(None)
        if len(s1) != len(s2):
            return False
        if s1 == s2:
            return True
        if sorted(s1) != sorted(s2):
            return False
        for i in range(1, len(s1)):
            if (self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:])) or (self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i])):
                return True
        return False
    
    
# @lc code=end

