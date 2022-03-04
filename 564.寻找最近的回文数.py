#
# @lc app=leetcode.cn id=564 lang=python3
#
# [564] 寻找最近的回文数
#

# @lc code=start
class Solution:
    def nearestPalindromic(self, n: str) -> str:
        l = len(n)
        if l == 1:
            return str(int(n) - 1)
        s = n[: l // 2 + l % 2]
        s1 = str(int(s) - 1)
        s2 = str(int(s) + 1)
        '''
        1.用原数的前半部分替换后半部分得到的回文整数。
        2.用原数的前半部分加一后的结果替换后半部分得到的回文整数。
        3.用原数的前半部分减一后的结果替换后半部分得到的回文整数。
        4.为防止位数变化导致构造的回文整数错误, 
        因此直接构造 999..999和 100..001 作为备选答案。
        '''
        return min(
            '9' * (l - 1),
            '1' + '0' * (l - 1) + '1',
            s + s[-1 - l % 2::-1],
            s1 + s1[-1 - l % 2::-1],
            s2 + s2[-1 - l % 2::-1],
            key=lambda x: (abs(int(x) - int(n)) or float('inf'), int(x))
        )
# @lc code=end


n = "11911"
sol = Solution().nearestPalindromic(n)
print(sol)
