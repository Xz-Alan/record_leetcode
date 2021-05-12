#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        num = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        total = 0
        for i in range(len(s) - 1):
            if num[s[i]] < num[s[i + 1]]:
                total -= num[s[i]]
            else:
                total += num[s[i]]
        total += num[s[i+1]]
        return total
            
# @lc code=end

